class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        memo ={}
        m = len(triangle)
       
        def dp(i,j):
            if i >= m or j>=len(triangle[i]):
                return 0
            state = (i,j)

            if state in memo:
                return memo[state]

            memo[state] = triangle[i][j] + min(dp(i+1,j),dp(i+1, j+1))
            return memo[state]

        return dp(0,0)
