# Problem: 01 Knapsack - https://www.geeksforgeeks.org/problems/0-1-knapsack-problem0945/1

import threading
from sys import setrecursionlimit

setrecursionlimit(1 << 30)
threading.stack_size(1 << 27)

class Solution:
    def knapsack(self, W, val, wt):
        n = len(val)
        memo = [[-1] * (W + 1) for _ in range(n)]

        def dp(i, remaining):
            if i < 0:
                return 0

            if memo[i][remaining] != -1:
                return memo[i][remaining]

            best = dp(i - 1, remaining)

            if wt[i] <= remaining:
                best = max(best, val[i] + dp(i - 1, remaining - wt[i]))

            memo[i][remaining] = best
            return best

        return dp(n - 1, W)
