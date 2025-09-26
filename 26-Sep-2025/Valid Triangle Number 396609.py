# Problem: Valid Triangle Number - https://leetcode.com/problems/valid-triangle-number/

class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        ans = 0

        def bs(left, target):
            right = n-1
            k = left-1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] < target:
                    k = mid        
                    left = mid + 1
                else:
                    right = mid - 1
            return k

        for i in range(n - 2):
            for j in range(i + 1, n - 1): 
                target = nums[i] + nums[j]
                ans += bs(j+1, target) - j

        return ans

