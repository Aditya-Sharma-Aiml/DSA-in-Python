class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        
        freq = defaultdict(int)
        n = len(nums)

        count = 0
        l, r = 0, 0

        for r in range(n):
            freq[nums[r]] += 1

            while freq[nums[r]] > k:
                freq[nums[l]] -= 1
                l+= 1
            count = max(count, r - l + 1)

        return count

        # Time Complexity O(n)
        # Space Complexity O(n)