# Problem: Frog Jump - https://leetcode.com/problems/frog-jump/

class Solution:
    def canCross(self, stones: List[int]) -> bool:
        memo = {}
        def dp(i, k):
            if i == len(stones)-1:
                return True

            state = (i, k)
            if state in memo:
                return memo[state]
            temp = False
            for j in range(i+1, len(stones)):
                if stones[j] == stones[i] + k-1:
                    temp = temp or dp(j, k-1)
                if stones[j] == stones[i] + k:
                    temp = temp or dp(j, k)
                if stones[j] == stones[i] + k+1:
                    temp = temp or dp(j, k+1)

            memo[state] = temp
            return temp
        return dp(0, 0)            

