# Problem: Decode Ways - https://leetcode.com/problems/decode-ways/

class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        memo = {}
        def dp(i):
            if i >= n:
                return 1
            if s[i] == "0":
                return 0
            
            if i in memo:
                return memo[i]
            
            memo[i] = dp(i+1)
            if i+2 <= n and int(s[i:i+2]) <= 26:
                memo[i] += dp(i+2)
            # memo[i] = dp(i+1) + dp(i+2)
            return memo[i]
        
        return dp(0)