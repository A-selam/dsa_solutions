# Problem: Solving Questions With Brainpower - https://leetcode.com/problems/solving-questions-with-brainpower/

class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        memo = {}
        n = len(questions)
        def dp(i):
            if i >= n:
                return 0
            
            if i in memo:
                return memo[i]
            
            currPoints, currPower = questions[i]
            memo[i] = max(dp(i+1), currPoints + dp(i+currPower+1))
            return memo[i]

        return dp(0)