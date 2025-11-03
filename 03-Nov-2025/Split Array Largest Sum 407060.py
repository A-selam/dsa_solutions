# Problem: Split Array Largest Sum - https://leetcode.com/problems/split-array-largest-sum/

class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        left = max(nums)
        right = sum(nums)
        ans = right

        while left <= right:
            mid = (left + right) // 2

            count = 0
            rs = 0
            for num in nums:
                rs += num
                if rs > mid:
                    count += 1
                    rs = num
            count += 1

            if count > k:
                left = mid + 1
            elif count <= k:
                right = mid - 1
                ans = min(ans, mid)

        return ans 