class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        res = [1] * len(nums)

        # Calculate prefix products
        for i in range(1, len(nums)):
            res[i] = res[i - 1] * nums[i - 1]
        
        # Calculate postfix products
        post = 1
        for i in range(len(nums) -2, -1, -1):
            post *= nums[i + 1]
            res[i] = res[i] * post
 
        return res

        # Time Complexity O(n)
        # Space Complexity O(n)