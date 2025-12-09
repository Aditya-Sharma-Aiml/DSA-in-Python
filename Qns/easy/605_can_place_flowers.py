class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        
        for i in range(len(flowerbed)):
            if n == 0:
                return True

            # Check conditions for planting a flower in the current plot:
            # 1. Either it's the first plot or the previous plot is empty
            # 2. Current plot is empty
            # 3. Either it's the last plot or the next plot is empty
            if ((i == 0 or flowerbed[i - 1] == 0)
            and flowerbed[i] == 0 
            and (i == len(flowerbed) -1 or flowerbed[i + 1] == 0)):
                flowerbed[i] = 1
                n -= 1

        return n == 0

        # Time Complexity O(n)
        # Space Complexity O(1)