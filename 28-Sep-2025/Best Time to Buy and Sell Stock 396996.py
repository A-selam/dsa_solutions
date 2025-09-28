# Problem: Best Time to Buy and Sell Stock - https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        memo = {}

        def dp(i, flag):
            if i >= n:
                return 0
            
            state = (i, flag)
            if state in memo:
                return memo[state]
            
            temp = dp(i+1, flag)
            if not flag:
                temp = max(temp, prices[i])
            else:
                temp = max(temp, dp(i+1, not flag) - prices[i])

            memo[state] = temp
            return temp
        
        return dp(0, True)