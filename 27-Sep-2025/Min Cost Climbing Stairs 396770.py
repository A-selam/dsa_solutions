# Problem: Min Cost Climbing Stairs - https://leetcode.com/problems/min-cost-climbing-stairs/

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        memo = dict()
        cost.append(0)

        def dp(i):
            if i == 0:
                return cost[0]
            if i == 1:
                return cost[1]
            
            if i not in memo:
                memo[i] = cost[i] + min(dp(i-1), dp(i-2))
            return memo[i]
        return dp(n)
