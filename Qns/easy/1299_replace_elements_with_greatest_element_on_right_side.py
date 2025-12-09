class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        maxx = -1

        for i in range(len(arr) -1, -1 , -1):
            tmp = arr[i]
            arr[i] = maxx                    
            maxx = max(maxx, tmp) 

        return arr

        # Time Complexity O(n)
        # Space Complexity O(1)