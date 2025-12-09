class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        
        dic = Counter(arr)
        occ = set()

        for item in dic.items():
            if item[1] in occ:
                return False
                
            occ.add(item[1])

        
        return True

        # Time Complexity O(n)
        # Space Complexity O(n)