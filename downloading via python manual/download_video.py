from pytubefix import YouTube
import os
import re
import subprocess

VIDEO_URL = "https://youtu.be/ogjf7ORKfd8?si=jcDKrLBKWfEODnHG"
OUTPUT_DIR = r"D:\Python Dsa\Videos\recursion_playlist"


def safe_filename(title: str) -> str:
    """Windows ke liye safe, chhota file name banata hai."""
    title = re.sub(r'[\\/*?:"<>|]', "", title)
    title = title.replace("\n", " ").replace("\r", " ")
    return (title.strip() or "video")[:80]


def on_progress(stream, chunk, bytes_remaining):
    total = stream.filesize or stream.filesize_approx
    downloaded = total - bytes_remaining
    percent = downloaded * 100 / total
    mb_total = total / (1024 * 1024)
    mb_down = downloaded / (1024 * 1024)
    print(
        f"\r   Downloading: {mb_down:.1f} / {mb_total:.1f} MB ({percent:.1f}%)",
        end="",
        flush=True,
    )


def run_ffmpeg_merge(video_path: str, audio_path: str, out_path: str):
    cmd = [
        "ffmpeg",
        "-y",
        "-i", video_path,
        "-i", audio_path,
        "-c", "copy",
        out_path,
    ]
    subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)


def download_with_retry(stream, output_path, filename, max_tries=3):
    for attempt in range(1, max_tries + 1):
        try:
            print(f"\n   Starting download ({attempt}/{max_tries}) -> {filename}")
            return stream.download(output_path=output_path, filename=filename)
        except Exception as e:
            print("\n   ❌ Download error:", e)
            if attempt == max_tries:
                raise


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    yt = YouTube(VIDEO_URL, on_progress_callback=on_progress)
    print("Title:", yt.title)

    base = safe_filename(yt.title)
    final_file = os.path.join(OUTPUT_DIR, base + ".mp4")

    if os.path.exists(final_file):
        print("✅ Already exists:", final_file)
        return

    # 1️⃣ Adaptive streams, but max 1080p (4K ko avoid kar rahe hain)
    try:
        print("\n🔹 Trying adaptive up to 1080p (stable best quality)...")

        all_video_streams = (
            yt.streams
            .filter(adaptive=True, only_video=True, file_extension="mp4")
            .order_by("resolution")
            .desc()
        )

        # Sirf woh stream rakho jinka resolution <= 1080p hai
        video_candidates = []
        for s in all_video_streams:
            if s.resolution:
                try:
                    h = int(s.resolution.replace("p", ""))
                    if h <= 1080:
                        video_candidates.append(s)
                except ValueError:
                    pass

        if not video_candidates:
            print("⚠️ No adaptive video <=1080p found, going to progressive fallback...")
            raise RuntimeError("No suitable adaptive video")

        print("   Adaptive candidate resolutions (<=1080p):",
              [s.resolution for s in video_candidates])

        audio_best = (
            yt.streams
            .filter(adaptive=True, only_audio=True, file_extension="mp4")
            .order_by("abr")
            .desc()
            .first()
        )

        if not audio_best:
            print("⚠️ No adaptive audio found, going to progressive fallback...")
            raise RuntimeError("No adaptive audio")

        # Pehle best audio download
        temp_audio_name = base + "_audio.mp4"
        temp_audio = os.path.join(OUTPUT_DIR, temp_audio_name)

        print("\n   Downloading best audio once...")
        download_with_retry(audio_best, OUTPUT_DIR, temp_audio_name)
        print()

        video_success = False
        for v_stream in video_candidates:
            print(f"\n   ▶ Trying video at {v_stream.resolution} ...")
            temp_video_name = base + f"_{v_stream.resolution}_video.mp4"
            temp_video = os.path.join(OUTPUT_DIR, temp_video_name)

            try:
                download_with_retry(v_stream, OUTPUT_DIR, temp_video_name)
                print()

                print("🎬 Merging with ffmpeg...")
                run_ffmpeg_merge(temp_video, temp_audio, final_file)

                os.remove(temp_video)
                os.remove(temp_audio)

                print("✅ DONE (adaptive <=1080p):", final_file)
                video_success = True
                break

            except Exception as e:
                print(f"   ❌ Failed at {v_stream.resolution}:", e)
                # delete partial file if exists
                if os.path.exists(temp_video):
                    os.remove(temp_video)
                continue  # try next lower resolution

        if video_success:
            return
        else:
            print("⚠️ All adaptive (<=1080p) failed, going to progressive fallback...")

    except Exception as e:
        print("\n⚠️ Adaptive method overall failed:")
        print("   Type:", type(e).__name__)
        print("   Msg :", e)
        print("👉 Falling back to progressive (720p max)...")

    # 2️⃣ Progressive fallback (simple + stable)
    try:
        yt2 = YouTube(VIDEO_URL, on_progress_callback=on_progress)
        p_stream = (
            yt2.streams
            .filter(progressive=True, file_extension="mp4")
            .order_by("resolution")
            .desc()
            .first()
        )

        if p_stream is None:
            print("❌ No progressive stream found. Cannot download this video.")
            return

        print(f"   Fallback progressive stream: {p_stream.resolution}")
        download_with_retry(p_stream, OUTPUT_DIR, os.path.basename(final_file))
        print()

        print("✅ DONE (progressive fallback):", final_file)

    except Exception as e:
        print("❌ COMPLETE FAIL for this video")
        print("   Type:", type(e).__name__)
        print("   Msg :", e)


if __name__ == "__main__":
    main()
