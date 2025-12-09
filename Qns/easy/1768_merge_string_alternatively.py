class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i = 0
        res = ""

        # Cycle until one of the string ends 
        while i < len(word1) and i < len(word2):
            res += word1[i] + word2[i]
            i += 1

        # Handling remaining characters
        if i < len(word1):
            res += word1[i:]
        else:
            res += word2[i:]

        return res
    
    # Time Complexity O(min(n, m)) 
    # Space Complexity O(m + n)
