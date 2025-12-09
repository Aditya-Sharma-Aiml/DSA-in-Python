class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        
        # Find the Max number of candies
        maxx = max(candies)
        res = [False] * len(candies)

        for i in range(len(candies)):
            # Check if is >= than max
            if candies[i] + extraCandies >= maxx:
                res[i] = True
        
        return res

        # Time Complexity O(n) 
        # Space Complexity O(n) 