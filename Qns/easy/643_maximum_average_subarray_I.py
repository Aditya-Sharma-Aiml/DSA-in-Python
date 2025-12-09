class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        
        # Find sum of k element
        currSum = maxSum = sum(nums[:k])

        for i in range(k, len(nums)):
            # Calculate the actual sum
            currSum += nums[i] - nums[i - k]
            maxSum = max(maxSum, currSum)

        # return the avg
        return maxSum / k
    
        # Time Complexity O(n)
        # Space Complexity O(1)        