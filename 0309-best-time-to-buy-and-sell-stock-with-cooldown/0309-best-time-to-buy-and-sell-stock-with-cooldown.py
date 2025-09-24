class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = {}
        def dp(i, f):
            if i >= len(prices):
                return 0
            state = (i, f)
            if state in memo:
                return memo[state]
            
            temp = dp(i+1, f)
            if f:
                temp = max(temp, dp(i+2, not f) + prices[i])
            else:
                temp = max(temp, dp(i+1, not f) - prices[i])
            
            memo[state] = temp
            return memo[state]
        return dp(0, False)