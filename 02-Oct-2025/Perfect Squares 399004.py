# Problem: Perfect Squares - https://leetcode.com/problems/perfect-squares/

class Solution:
    def numSquares(self, n: int) -> int:
        psqr = []
        for i in range(1, n+1):
            temp = isqrt(i)
            if temp * temp == i:
                psqr.append(i)
        
        dp = [inf] * (n+1)
        dp[0] = 0
        dp[1] = 1

        for i in range(1, n+1):
            for j in psqr:
                if j > i:
                    break
                dp[i] = min(dp[i], 1+dp[i-j])
        
        return dp[-1]