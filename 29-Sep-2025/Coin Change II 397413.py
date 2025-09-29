# Problem: Coin Change II - https://leetcode.com/problems/coin-change-ii/

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        memo = {}

        def dp(i, remain):
            if remain == 0:
                return 1
            if i == len(coins) or remain < 0:
                return 0

            state = (i, remain)
            if state in memo:
                return memo[state]

            take = dp(i, remain - coins[i])
            skip = dp(i+1, remain)

            memo[state] = take + skip
            return memo[state]

        return dp(0, amount)
