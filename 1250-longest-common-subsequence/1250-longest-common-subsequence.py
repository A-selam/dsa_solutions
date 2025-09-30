class Solution:
    def longestCommonSubsequence(self, s: str, t: str) -> int:
        n, m = len(s), len(t)

        memo = [[0] * (m) for _ in range(n)]
        for i in range(n-1, -1, -1):
            for j in range(m-1, -1, -1):
                if s[i] == t[j]:
                    memo[i][j] = 1 + (memo[i+1][j+1] if i+1 < n and j+1 < m else 0)
                else:
                    notTaken = 0
                    if i+1 < n:
                        notTaken = memo[i+1][j]
                    if j+1 < m:
                        notTaken = max(notTaken, memo[i][j+1])
                    memo[i][j] = notTaken
        return (memo[0][0])