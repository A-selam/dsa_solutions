# Problem: Minimum Score Triangulation of Polygon - https://leetcode.com/problems/minimum-score-triangulation-of-polygon/

class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:
        memo = {}
        def dp(i, j):
            if i + 2 > j:
                return 0
            if i + 2 == j:
                return values[i] * values[i + 1] * values[j]
            
            state = (i, j)
            if state in memo:
                return memo[state]

            temp = inf
            for k in range(i+1, j):
                temp = min(temp, values[i]*values[j]*values[k] + dp(i, k) + dp(k, j))
            
            memo[state] = temp
            return temp

        return(dp(0, len(values)-1))