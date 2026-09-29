'''
we maintain a clock timer, set to t=0
We have a grid
We see whixh element has value =2
We then like check all the three remaining adjacent values to check for 1
Once we find it and if not in visited, we increment the timer by 1
Add the visited nodes in visited array
Repeat Recursively 
'''
from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols= len(grid), len(grid[0])
        q=deque()
        fresh=0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==1:
                    fresh+=1
                elif grid[r][c]==2:
                    q.append((r,c))
        minutes=0
        while q and fresh>0:
            for _ in range(len(q)):
                r,c=q.popleft()
                for dr, dc in ((-1,0),(0,-1),(1,0),(0,1)):
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        fresh -= 1
                        q.append((nr, nc))
            minutes += 1

        return minutes if fresh == 0 else -1


    
        



    



    
