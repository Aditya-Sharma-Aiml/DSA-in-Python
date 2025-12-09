class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:

        row_counts = collections.defaultdict(int)  # Store row frequencies
        count = 0

        # Count occurrences of each row:
        for row in grid:
            row_tuple = tuple(row)
            row_counts[row_tuple] += 1

        # Check columns against row counts:
        for col_index in range(len(grid[0])):
            column = tuple(grid[row_index][col_index] for row_index in range(len(grid)))
            count += row_counts[column]

        return count

        # Time complexity: O(n^2)
        # Space complexity: O(n)