class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        memo = {}
        def dp(i, j):
            if i == n-1 and j == m-1:
                return grid[i][j]
            if i == n or j == m:
                return float('inf')
            
            state = (i, j)
            if state in memo:
                return memo[state]
            
            memo[state] = grid[i][j] + min(dp(i+1, j), dp(i, j+1))
            return memo[state]
        return dp(0,0)