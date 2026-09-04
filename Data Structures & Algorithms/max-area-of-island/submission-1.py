from typing import List
from collections import deque

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        rows, columns = len(grid), len(grid[0])
        visited = set()
        max_area = 0

        for r in range(rows):
            for c in range(columns):
                if grid[r][c] == 1 and (r, c) not in visited:
                    area = 0
                    queue = deque([(r, c)])
                    visited.add((r, c))
                    while queue:
                        cr, cc = queue.popleft()
                        area += 1
                        for dr, dc in ((1,0), (-1,0), (0,1), (0,-1)):
                            nr, nc = cr + dr, cc + dc
                            if 0 <= nr < rows and 0 <= nc < columns \
                                    and grid[nr][nc] == 1 and (nr, nc) not in visited:
                                visited.add((nr, nc))
                                queue.append((nr, nc))
                    max_area = max(max_area, area)

        return max_area
        