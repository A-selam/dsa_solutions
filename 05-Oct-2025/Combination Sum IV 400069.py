# Problem: Combination Sum IV - https://leetcode.com/problems/combination-sum-iv/description/

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        n = len(nums)
        memo = {}
        def dp(s):
            if s == target:
                return 1
            if s > target:
                return 0
            
            if s in memo:
                return memo[s]

            temp = 0
            for j in range(0, n):
                temp += dp(s+nums[j])
            
            memo[s] = temp
            return temp
        return dp(0)