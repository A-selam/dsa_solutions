# Problem: Word Break - https://leetcode.com/problems/word-break/description/

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = {}
        wordSet = set(wordDict)

        def dp(start):
            if start == len(s):
                return True
            if start in memo:
                return memo[start]

            for end in range(start+1, len(s)+1):
                if s[start:end] in wordSet and dp(end):
                    memo[start] = True
                    return True

            memo[start] = False
            return False
        return dp(0) 