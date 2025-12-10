from pytubefix import Playlist
import os
import re
import subprocess

PLAYLIST_URL = "https://www.youtube.com/playlist?list=PLgUwDviBIf0rGlzIn_7rsaR2FQ5e6ZOL9"
OUTPUT_DIR = r"D:\Python Dsa\Videos"


def safe_filename(title: str) -> str:
    title = re.sub(r'[\\/*?:"<>|]', "", title)
    title = title.replace("\n", " ").replace("\r", " ")
    return title.strip() or "video"


os.makedirs(OUTPUT_DIR, exist_ok=True)

pl = Playlist(PLAYLIST_URL)
print(f"Playlist: {pl.title}")
print(f"Total videos: {len(pl.videos)}")

for i, video in enumerate(pl.videos, start=1):
    print("\n===================================")
    print(f"[{i}/{len(pl.videos)}] {video.title}")

    try:
        # 🔹 Highest resolution video
        v_stream = (
            video.streams
            .filter(adaptive=True, only_video=True, file_extension="mp4")
            .order_by("resolution")
            .desc()
            .first()
        )

        # 🔹 Highest quality audio
        a_stream = (
            video.streams
            .filter(adaptive=True, only_audio=True, file_extension="mp4")
            .order_by("abr")
            .desc()
            .first()
        )

        if v_stream is None or a_stream is None:
            print("⚠️ Stream nahi mili, skipping...")
            continue

        print("Video:", v_stream.resolution, "| Audio:", a_stream.abr)

        base = safe_filename(video.title)
        temp_video = os.path.join(OUTPUT_DIR, base + "_video.mp4")
        temp_audio = os.path.join(OUTPUT_DIR, base + "_audio.mp4")
        final_file = os.path.join(OUTPUT_DIR, base + ".mp4")

        if os.path.exists(final_file):
            print("✅ Already exists, skipping:", final_file)
            continue

        print("⬇️ Downloading video...")
        v_stream.download(output_path=OUTPUT_DIR, filename=os.path.basename(temp_video))

        print("⬇️ Downloading audio...")
        a_stream.download(output_path=OUTPUT_DIR, filename=os.path.basename(temp_audio))

        print("🎬 Merging with ffmpeg...")
        cmd = [
            "ffmpeg",
            "-y",
            "-i", temp_video,
            "-i", temp_audio,
            "-c", "copy",
            final_file,
        ]
        subprocess.run(cmd, check=True)

        os.remove(temp_video)
        os.remove(temp_audio)

        print("✅ Saved:", final_file)

    except Exception as e:
        print("❌ Failed:", video.watch_url, "->", e)
from pytubefix import Playlist
import os
import re
import subprocess

PLAYLIST_URL = "https://www.youtube.com/playlist?list=PLgUwDviBIf0rGlzIn_7rsaR2FQ5e6ZOL9"
OUTPUT_DIR = r"D:\Python Dsa\Highest_Videos"


def safe_filename(title: str) -> str:
    title = re.sub(r'[\\/*?:"<>|]', "", title)
    title = title.replace("\n", " ").replace("\r", " ")
    return title.strip() or "video"


os.makedirs(OUTPUT_DIR, exist_ok=True)

pl = Playlist(PLAYLIST_URL)
print(f"Playlist: {pl.title}")
print(f"Total videos: {len(pl.videos)}")

for i, video in enumerate(pl.videos, start=1):
    print("\n===================================")
    print(f"[{i}/{len(pl.videos)}] {video.title}")

    try:
        # 🔹 Highest resolution video
        v_stream = (
            video.streams
            .filter(adaptive=True, only_video=True, file_extension="mp4")
            .order_by("resolution")
            .desc()
            .first()
        )

        # 🔹 Highest quality audio
        a_stream = (
            video.streams
            .filter(adaptive=True, only_audio=True, file_extension="mp4")
            .order_by("abr")
            .desc()
            .first()
        )

        if v_stream is None or a_stream is None:
            print("⚠️ Stream nahi mili, skipping...")
            continue

        print("Video:", v_stream.resolution, "| Audio:", a_stream.abr)

        base = safe_filename(video.title)
        temp_video = os.path.join(OUTPUT_DIR, base + "_video.mp4")
        temp_audio = os.path.join(OUTPUT_DIR, base + "_audio.mp4")
        final_file = os.path.join(OUTPUT_DIR, base + ".mp4")

        if os.path.exists(final_file):
            print("✅ Already exists, skipping:", final_file)
            continue

        print("⬇️ Downloading video...")
        v_stream.download(output_path=OUTPUT_DIR, filename=os.path.basename(temp_video))

        print("⬇️ Downloading audio...")
        a_stream.download(output_path=OUTPUT_DIR, filename=os.path.basename(temp_audio))

        print("🎬 Merging with ffmpeg...")
        cmd = [
            "ffmpeg",
            "-y",
            "-i", temp_video,
            "-i", temp_audio,
            "-c", "copy",
            final_file,
        ]
        subprocess.run(cmd, check=True)

        os.remove(temp_video)
        os.remove(temp_audio)

        print("✅ Saved:", final_file)

    except Exception as e:
        print("❌ Failed:", video.watch_url, "->", e)
from pytubefix import Playlist
import os
import re
import subprocess

PLAYLIST_URL = "https://www.youtube.com/playlist?list=PLgUwDviBIf0rGlzIn_7rsaR2FQ5e6ZOL9"
OUTPUT_DIR = r"D:\Python Dsa\Highest_Videos"


def safe_filename(title: str) -> str:
    title = re.sub(r'[\\/*?:"<>|]', "", title)
    title = title.replace("\n", " ").replace("\r", " ")
    return title.strip() or "video"


os.makedirs(OUTPUT_DIR, exist_ok=True)

pl = Playlist(PLAYLIST_URL)
print(f"Playlist: {pl.title}")
print(f"Total videos: {len(pl.videos)}")

for i, video in enumerate(pl.videos, start=1):
    print("\n===================================")
    print(f"[{i}/{len(pl.videos)}] {video.title}")

    try:
        # 🔹 Highest resolution video
        v_stream = (
            video.streams
            .filter(adaptive=True, only_video=True, file_extension="mp4")
            .order_by("resolution")
            .desc()
            .first()
        )

        # 🔹 Highest quality audio
        a_stream = (
            video.streams
            .filter(adaptive=True, only_audio=True, file_extension="mp4")
            .order_by("abr")
            .desc()
            .first()
        )

        if v_stream is None or a_stream is None:
            print("⚠️ Stream nahi mili, skipping...")
            continue

        print("Video:", v_stream.resolution, "| Audio:", a_stream.abr)

        base = safe_filename(video.title)
        temp_video = os.path.join(OUTPUT_DIR, base + "_video.mp4")
        temp_audio = os.path.join(OUTPUT_DIR, base + "_audio.mp4")
        final_file = os.path.join(OUTPUT_DIR, base + ".mp4")

        if os.path.exists(final_file):
            print("✅ Already exists, skipping:", final_file)
            continue

        print("⬇️ Downloading video...")
        v_stream.download(output_path=OUTPUT_DIR, filename=os.path.basename(temp_video))

        print("⬇️ Downloading audio...")
        a_stream.download(output_path=OUTPUT_DIR, filename=os.path.basename(temp_audio))

        print("🎬 Merging with ffmpeg...")
        cmd = [
            "ffmpeg",
            "-y",
            "-i", temp_video,
            "-i", temp_audio,
            "-c", "copy",
            final_file,
        ]
        subprocess.run(cmd, check=True)

        os.remove(temp_video)
        os.remove(temp_audio)

        print("✅ Saved:", final_file)

    except Exception as e:
        print("❌ Failed:", video.watch_url, "->", e)
