class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        counts = [0, 0]

        for s in students:
            counts[s] += 1

        remaining = len(sandwiches)
        for s in sandwiches:
            if counts[s] == 0:
                break
            if remaining == 0:
                break

            counts[s] -= 1
            remaining -= 1
        
        return remaining

        # Time Complexity O(n)
        # Space Complexity O(1)