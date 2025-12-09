class Solution:
    def maxDepth(self, s: str) -> int:
        maxx = 0
        depth = 0

        for c in s:
            if c == "(":
                depth += 1           

            if c == ")":
                depth -= 1

            maxx = max(maxx, depth)
        
        return maxx

        # Time Complexity O(n)
        # Space Complexity O(1)