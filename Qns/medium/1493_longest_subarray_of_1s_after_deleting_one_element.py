class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left = 0
        zeroIndex = -1
        maxLength = 0
        
        for right in range(len(nums)):
            if nums[right] == 0:
                left = zeroIndex + 1
                zeroIndex = right

            maxLength = max(maxLength, right - left + 1)
        
        return maxLength - 1 if maxLength else 0

        # Time Complexity O(n)
        # Space Complexity O(1)