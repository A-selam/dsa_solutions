class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        dir = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        left = grid[0][0]
        right = 0
        for i in range(n):
            right = max(right, max(grid[i]))

        def inBound(row, col):
            return 0 <= row < n and 0 <= col < m
        
        def dfs_iterative(i, j, time):
            if grid[i][j] > time:
                return False
            stack = [(i, j)]
            visited = set([(i, j)])

            while stack:
                row, col = stack.pop()
                if row == n-1 and col == m-1:
                    return True
                for r, c in dir:
                    newR = row+r
                    newC = col+c
                    if inBound(newR, newC) and (newR, newC) not in visited and grid[newR][newC] <= time:
                        visited.add((newR, newC))
                        stack.append((newR, newC))
            return False

        while left < right:
            mid = (left + right)//2
            if dfs_iterative(0, 0, mid):
                right = mid
            else:
                left = mid+1
        return left