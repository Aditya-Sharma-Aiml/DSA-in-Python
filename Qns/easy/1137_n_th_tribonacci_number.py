# Dynamic programming solution
class Solution:
    def tribonacci(self, n: int) -> int:
        t = [0, 1, 1]

        if n < 3:
            return t[n]

        for i in range(3, n + 1):
            t[0], t[1], t[2] = t[1], t[2], sum(t)
            
        return t[2]

        # Time Complexity O(n)
        # Space Complexity O(1)

# Memoization solution
class Solution:
    def tribonacci(self, n: int) -> int:
        
        def helper(n):

            if n in dic:
                return dic[n]

            if n == 0:
                return 0

            if n == 1 or n == 2:
                return 1

            if n >= 0:
                dic[n] = helper(n - 1) + helper(n - 2) + helper(n -3)
                return dic[n]

        dic = {}
        return helper(n)

        # Time Complexity O(n)
        # Space Complexity O(n)