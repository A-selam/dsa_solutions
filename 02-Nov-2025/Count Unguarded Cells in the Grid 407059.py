# Problem: Count Unguarded Cells in the Grid - https://leetcode.com/problems/count-unguarded-cells-in-the-grid/

class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        grid = [[0] * n for _ in range(m)]
        checked = set()

        for row, col in walls:
            grid[row][col] = 1
        for row, col in guards:
            grid[row][col] = 2
        
        def checker(row, col):
            for i in range(row+1, m):
                if grid[i][col] > 0:
                    break
                checked.add((i, col))
            for i in range(row-1, -1, -1):
                if grid[i][col] > 0:
                    break
                checked.add((i, col))
            for j in range(col+1, n):
                if grid[row][j] > 0:
                    break
                checked.add((row, j))
            for j in range(col-1, -1, -1):
                if grid[row][j] > 0:
                    break
                checked.add((row, j))
        
        for row, col in guards:
            checker(row, col)
        return (m*n) - len(checked) - len(guards) - len(walls)