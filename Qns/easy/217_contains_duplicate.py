class Solution(object):
    def containsDuplicate(self, nums):

        mapp = set()
        for n in nums:
            if n in mapp:
                return True
            mapp.add(n)

        return False

        # Time Complexity O(n)
        # Space Complexity O(n)
    

class Solution(object):
    def containsDuplicate(self, nums):
        
        mapp = list(set(nums))
        if len(mapp) == len(nums):
            return False
        return True

        # Time Complexity O(n)
        # Space Complexity O(n)