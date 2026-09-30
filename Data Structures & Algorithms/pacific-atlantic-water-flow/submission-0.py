'''
1)We use DFS in this question
2)Given a particular cell we check if any of the neighbouring cells are already in the result array; if they are greater than them then automatically add to result
3) If not, then check if a cell has a neighbouring cell with height lesser than and check if that cell is somehow connected to the other side and repeat recursively
'''
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols= len(heights), len(heights[0])
        def spread(seeds):
            reach= set(seeds)
            queue=deque(seeds)
            while queue:
                r,c = queue.popleft()
                for dr, dc in ((1,0), (0,1), (-1,0), (0,-1)):
                    nr, nc= r+dr, c+dc
                    if (0<=nr< rows and 0<=nc<cols and (nr,nc) not in reach and heights[nr][nc]>= heights[r][c]):
                        reach.add((nr,nc))
                        queue.append((nr, nc))
            return reach 
        pacific_seeds = [(0, c) for c in range(cols)] + [(r, 0) for r in range(rows)]
        atlantic_seeds = [(rows - 1, c) for c in range(cols)] + [(r, cols - 1) for r in range(rows)]

        pacific = spread(pacific_seeds)
        atlantic = spread(atlantic_seeds)

        result = pacific & atlantic
        return [[r, c] for r, c in result]




                 
            

    


        