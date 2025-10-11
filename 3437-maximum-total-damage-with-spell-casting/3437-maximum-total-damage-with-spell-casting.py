class Solution:
    def maximumTotalDamage(self, power):
        count = Counter(power)
        nums = sorted(count.keys())
        n = len(nums)

        @lru_cache(None)
        def dp(i):
            if i == n:
                return 0
            
            res = dp(i + 1)

            next_i = i + 1
            while next_i < n and nums[next_i] <= nums[i] + 2:
                next_i += 1
            
            res = max(res, count[nums[i]] * nums[i] + dp(next_i))
            return res

        return dp(0)
