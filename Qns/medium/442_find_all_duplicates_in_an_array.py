class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res = []

        for i in range(len(nums)):
            num = abs(nums[i])
            idx = num - 1
            
            if nums[idx] < 0:
                res.append(num)

            nums[idx] *= -1

        return res

        # Time Complexity O(n)
        # Space Complexity O(1)
