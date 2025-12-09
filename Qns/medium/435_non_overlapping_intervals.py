class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        intervals.sort()
        count = 0
        prev_end = intervals[0][1]

        for start, end in intervals[1:]:
            # If the current interval overlaps with the previous one, remove the current interval
            if start < prev_end:
                count += 1
                prev_end = min(end, prev_end)
            else:
                # Update the end time for the next iteration
                prev_end = end                            

        return count

        # Time Complexity O(nlogn)
        # Space Complexity O(1)