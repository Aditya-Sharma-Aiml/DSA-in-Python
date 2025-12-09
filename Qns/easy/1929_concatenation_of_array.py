class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)

        for i in range(n):
            nums.append(nums[i])

        return nums

        # Time Complexity O(n)
        # Space Complexity O(n)
    
class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        
        return nums * 2

class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = []
        for i in range(2):
            for n in nums:
                ans.append(n)
        return ans
    