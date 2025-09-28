# Problem: Best Sightseeing Pair - https://leetcode.com/problems/best-sightseeing-pair/

from typing import List

class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        n = len(values)
        memo = {}

        def dp(j, bestPrev):
            if j == n:
                return float("-inf")

            if (j, bestPrev) in memo:
                return memo[(j, bestPrev)]

            score = values[j] - j + bestPrev 

            newBestPrev = max(bestPrev, values[j] + j)
            score = max(score, dp(j + 1, newBestPrev))

            memo[(j, bestPrev)] = score
            return score

        return dp(1, values[0])
