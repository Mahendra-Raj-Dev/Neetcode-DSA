# Problem: N-Queens
# Pattern: Backtracking (DFS with constraints)
# Idea:
# - Place one queen per row
# - Track used columns and diagonals (posDiag, negDiag)
# - Skip invalid positions
# - Backtrack after each placement
# Time: O(N!)   (approx, pruning reduces search)
# Space: O(N)   (sets + recursion stack + board)

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col = set()
        posDiag = set()
        negDiag = set()
        res = []
        board = [["."] * n for i in range(n)]
        def dfs(r):
            if r == n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return 
            
            for c in range(n):
                if c in col or (r + c) in posDiag or (r - c) in negDiag:
                    continue
                
                col.add(c)
                posDiag.add(r + c)
                negDiag.add(r - c)
                board[r][c] = "Q"
                dfs(r + 1)

                col.remove(c)
                posDiag.remove(r + c)
                negDiag.remove(r - c)
                board[r][c] = "."
        dfs(0)
        return res