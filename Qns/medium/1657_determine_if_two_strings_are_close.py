class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if word1 == word2:
            return True

        if len(word1) != len(word2):
            return False

        w1_counter = Counter(word1)
        w2_counter = Counter(word2)

        # Check if character sets differ
        if len(w1_counter.keys() - w2_counter.keys()) != 0:
            return False

        # Sort for comparison of char frequency
        w1 = sorted(w1_counter.values())
        w2 = sorted(w2_counter.values())

        return w1 == w2

        # Time Complexity O(n)
        # Space Complexity O(m + n)