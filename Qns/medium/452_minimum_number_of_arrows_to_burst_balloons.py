
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:

        # Sort balloons based on ending positions
        points.sort(key=lambda x: x[1])
        prev_end = points[0][1]
        arrows = 1

        for start, end in points[1:]:
            if start > prev_end:
                prev_end = end
                arrows += 1

        return arrows

        # Time Complexity O(nlogn)
        # Space Complexity O(1)

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        
        # Sort balloons based on starting positions
        points.sort()
        prev_end = points[0][1]
        arrows = 1       

        for start, end in points[1:]:
            if prev_end >= start:
                prev_end = min(prev_end, end)

            else:
                arrows += 1
                prev_end = end
        
        return arrows
    
        # Time Complexity O(nlogn)
        # Space Complexity O(1)