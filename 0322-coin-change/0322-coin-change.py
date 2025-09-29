class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        memo[0] = 0

        for amt in range(1, amount+1):
            ans = inf
            for coin in coins:
                if coin <= amt:
                    ans = min(ans, memo[amt-coin]+1)
            memo[amt] = ans
        
        return memo[amount] if memo[amount] != inf else -1