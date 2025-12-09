class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:

        if k <= 1:
            return 0

        cnt = 0
        prod = 1
        left = 0

        for right in range(len(nums)):
            prod *= nums[right]

            while prod >= k and left <= right:
                prod //= nums[left]
                left += 1

            cnt += right - left + 1
        return cnt

        # Time Complexity O(n)
        # Space Complexity O(1)