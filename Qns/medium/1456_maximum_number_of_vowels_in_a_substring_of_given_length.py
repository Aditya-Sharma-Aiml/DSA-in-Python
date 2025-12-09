class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set("aeiou")
        cnt = 0
        res = 0

        # Count how many vowels are in the initial window of size k
        for i in range(k):
            if s[i] in vowels:
                cnt += 1
                res += 1

        # Optimization: Early exit if initial window has all vowels
        if res != k:
            # Slide the window and update vowel count efficiently
            for i in range(k, len(s)):
                cnt += (s[i] in vowels) - (s[i - k] in vowels)
                res = max(cnt, res)

                # Early exit if window has all vowels
                if res == k:
                    break

        return res

        # Time Complexity: O(n)
        # Space Complexity: O(1)