# Problem: Triangle - https://leetcode.com/problems/triangle/

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle[-1])
        dp = [[inf] * n for _ in range(n)]
        dp[0][0] = triangle[0][0]

        for i in range(1, n):
            for j in range(i+1):
                dp[i][j] = dp[i-1][j]
                if j > 0:
                    dp[i][j] = min(dp[i][j], dp[i-1][j-1])
                dp[i][j] += triangle[i][j]
        return min(dp[-1])


        # memo ={}
        # m = len(triangle)
       
        # def dp(i,j):
        #     if i >= m or j>=len(triangle[i]):
        #         return 0
        #     state = (i,j)

        #     if state in memo:
        #         return memo[state]

        #     memo[state] = triangle[i][j] + min(dp(i+1,j),dp(i+1, j+1))
        #     return memo[state]

        # return dp(0,0)
