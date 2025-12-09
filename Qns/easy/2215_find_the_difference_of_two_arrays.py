class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        
        s1 = set(nums1)
        s2 = set(nums2)

        res1 = set()
        res2 = set()

        for n in nums1:
            if n not in s2:
                res1.add(n)

        for n in nums2:
            if n not in s1:
                res2.add(n)

        return [list(res1), list(res2)]

        # Time Complexity O(max(n, m))
        # Space Complexity O(n + m)