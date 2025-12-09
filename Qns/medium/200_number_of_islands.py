class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0

        rows = len(grid)
        cols = len(grid[0])

        island = 0
        visit = set()

        def dfs(r, c):
            if (r not in range(rows) or 
                c not in range(cols) or
                (r, c) in visit or
                grid[r][c] == "0"):
                return 

            visit.add((r,c))
            directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            for dr, dc in directions:
                dfs(r + dr, c + dc)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visit:
                    island += 1
                    dfs(r, c)

        return island

        # Time Complexity O(n*m)
        # Space Complexity O(n*m)