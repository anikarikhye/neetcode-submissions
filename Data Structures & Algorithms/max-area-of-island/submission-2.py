from typing import List

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        rows, columns = len(grid), len(grid[0])
        visited = set()
        max_area = 0

        def explore(r, c):
            if r < 0 or r >= rows or c < 0 or c >= columns:
                return 0
            if grid[r][c] == 0 or (r, c) in visited:
                return 0
            visited.add((r, c))
            return (1
                    + explore(r + 1, c)
                    + explore(r - 1, c)
                    + explore(r, c + 1)
                    + explore(r, c - 1))

        for r in range(rows):
            for c in range(columns):
                if grid[r][c] == 1 and (r, c) not in visited:
                    area = explore(r, c)
                    max_area = max(max_area, area)

        return max_area
        