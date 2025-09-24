class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}
        def dp(i, curr):
            if i == len(nums) and curr == target:
                return 1
            if i == len(nums) and curr != target:
                return 0
            
            state = (i, curr)
            if state not in memo:
                memo[state] = dp(i+1, curr + nums[i]) + dp(i+1, curr - nums[i])
            return memo[state]
        return dp(0, 0)