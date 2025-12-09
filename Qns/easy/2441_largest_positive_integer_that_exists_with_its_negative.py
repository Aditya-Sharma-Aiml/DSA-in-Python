# hashset
class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        hashset = set(nums)
        res = -1

        for n in nums:
            if n * -1 in hashset:
                res = max(res, n)

        return res

        # Time Complexity O(n)
        # Space Complexity O(n)

# Sorting + 2 pointer
class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        nums.sort()
        l, r = 0, len(nums) - 1

        while l < r:
            if nums[l] + nums[r] == 0:
                return nums[r]
            
            elif nums[l] + nums[r] > 0:
                r -= 1
            
            else:
                l += 1

        return -1

        # Time Complexity O(nlogn)
        # Space Complexity O(1)
