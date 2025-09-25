class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        memo = {}
        def dp(i):
            if i+len(word) > len(sequence):
                return 0

            if i in memo:
                return memo[i]
            
            if sequence[i:i+len(word)] == word:
                memo[i] = 1+dp(i+len(word))
            else:
                memo[i] = 0

            return memo[i]

        ans = 0
        for i in range(len(sequence)):
            ans = max(ans, dp(i))
        return ans
