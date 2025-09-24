class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        memo = {}
        def dp(tot):
            if tot >= amount:
                return 0
            if tot in memo:
                return memo[tot]

            temp = float('inf')
            for coin in coins:
                if tot+coin <= amount:
                    temp = min(temp, 1+dp(tot+coin))
            memo[tot] = temp
            return memo[tot]
        ans = dp(0)
        return ans if ans != float('inf') else -1