# Problem: Stone Game - https://leetcode.com/problems/stone-game/

class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        n = len(piles)
        memo = [[0]*n for _ in range(n)]

        for i in range(n):
            memo[i][i] = piles[i]
        
        for length in range(2, n+1):
            for l in range(0, n-length+1):
                r = l + length-1
                memo[l][r] = max(piles[l] - memo[l+1][r], piles[r] - memo[l][r-1])
        return memo[0][n-1] > 0

        # def dp(l, r):
        #     if l == r:
        #         return piles[l]
        #     if (l, r) in memo:
        #         return memo[(l, r)]
            
        #     pick_left = piles[l] - dp(l + 1, r)
        #     pick_right = piles[r] - dp(l, r - 1)

        #     memo[(l, r)] = max(pick_left, pick_right)
        #     return memo[(l, r)]
        
        # return dp(0, n - 1) > 0
