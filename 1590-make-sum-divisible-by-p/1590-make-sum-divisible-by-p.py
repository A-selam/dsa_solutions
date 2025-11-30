class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        n = len(nums)
        sum_ = sum(nums)
        target = sum_ % p

        if target == 0:
            return 0
        
        pre = 0
        dic = {0: -1}
        ans = inf
        for i, num in enumerate(nums):
            pre = (pre+num)%p
            if (pre-target)%p in dic:
                ans = min(ans, i-dic[(pre-target)%p])
            dic[pre] = i
        
        if ans == n:
            return -1

        return ans