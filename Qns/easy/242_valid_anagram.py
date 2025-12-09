class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        dict1 = defaultdict(int)
        dict2 = defaultdict(int)

        if len(s) != len(t):
            return False

        for c in range(len(s)):
            dict1[s[c]] += 1
            dict2[t[c]] += 1

        return dict1 == dict2

        # Time Complexity O(s)
        # Space Complexity O(s + t)
    
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        return sorted(s) == sorted(t)
    
        # Time Complexity O(nlogn)
        # Space Complexity O(1)