class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:        
        dic = {}

        for i, n in enumerate(nums):
            # Find the complement
            compl = target - n
            # if the complement is in dic it's possible to return
            if compl in dic:
                return [i, dic[compl]]
            dic[n] = i

        # Time complexity O(n)
        # Space complexity O(n)