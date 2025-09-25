# Problem: Coin Change - https://leetcode.com/problems/coin-change/

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        if amount == 0:
            return 0

        coins.sort()
        coins.reverse()
        memo = {}

        def dp(i, tot):
            if tot == amount:
                return 0
            if i == n:
                return float('inf')

            state = (i, tot)
            if state in memo:
                return memo[state]
            
            temp = dp(i+1, tot)
            if tot + coins[i] <= amount:
                temp = min(temp, 1+dp(i, tot+coins[i]))
            
            memo[state] = temp
            return memo[state]

        ans = dp(0,0)
        return ans if ans != float('inf') else -1