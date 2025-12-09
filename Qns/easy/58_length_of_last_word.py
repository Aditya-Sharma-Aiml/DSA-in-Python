class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # Remove spaces at the end of the string
        s = s.rstrip()

        cnt = 0
        for i in range(len(s) - 1, -1, -1):
            if s[i] != ' ' and s:
                cnt += 1
            else:
                return cnt
        return cnt


        # Time Complexity O(n)
        # Space Complexity O(1)

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.split()[-1])