class Solution:
    def tribonacci(self, n: int) -> int:
        memo = {}
        def dp(i):
            if i == 0 or i == 1:
                return i
            if i == 2:
                return 1
            if i in memo:
                return memo[i]
            
            memo[i] = dp(i-1) + dp(i-2) + dp(i-3)
            return memo[i]
        return dp(n)