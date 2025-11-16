# Problem: Unique Paths III - https://leetcode.com/problems/unique-paths-iii/

class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        ans = 0

        start = end = (0, 0)
        count = 0

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    start = (i, j)
                elif grid[i][j] == 2:
                    end = (i, j)
                elif grid[i][j] == 0:
                    count += 1

        dir = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def inBound(row, col):
            return 0 <= row < n and 0 <= col < m

        def bt(row, col, vis):
            nonlocal ans
            if row == end[0] and col == end[1]:
                if len(vis) == count + 2:
                    ans += 1
                return 
            
            for i, j in dir:
                newRow = row + i
                newCol = col + j

                if inBound(newRow, newCol) and grid[newRow][newCol] != -1 and (newRow, newCol) not in vis:
                    vis.add((newRow, newCol))
                    bt(newRow, newCol, vis)
                    vis.remove((newRow, newCol))
        
        vis = set([(start[0], start[1])])
        bt(start[0], start[1], vis)
        return ans