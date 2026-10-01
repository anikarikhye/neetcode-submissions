from collections import deque
from typing import List

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board), len(board[0])
        q = deque()

        # 1) Mark border 'O's as 'B' and queue them
        for row in range(rows):
            for column in range(cols):
                if row == 0 or row == rows - 1 or column == 0 or column == cols - 1:
                    if board[row][column] == "O":
                        board[row][column] = "B"
                        q.append((row, column))

        # 2) Spread 'B' to every connected 'O'
        while q:
            row, column = q.popleft()
            for dr, dc in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                nr, nc = row + dr, column + dc
                if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] == "O":
                    board[nr][nc] = "B"
                    q.append((nr, nc))

        # 3) Remaining 'O' are surrounded -> 'X'; 'B' goes back to 'O'
        for row in range(rows):
            for column in range(cols):
                if board[row][column] == "O":
                    board[row][column] = "X"
                elif board[row][column] == "B":
                    board[row][column] = "O"

                
                        


     
                
            
        
        





        





        