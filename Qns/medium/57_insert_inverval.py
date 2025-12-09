class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []

        # 3 cases:
        # - newInterval < intervals
        # - newInterval > intervals
        # - newInterval overlaps with intervals
        for i in range(len(intervals)):
            # first case
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:]
            # second case 
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i])
            # third case
            else:
                newInterval[0] = min(newInterval[0], intervals[i][0])
                newInterval[1] = max(newInterval[1], intervals[i][1])

        res.append(newInterval)
        return res
    
        # Time Complexity O(n) 
        # Space Complexity O(n)