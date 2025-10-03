# Problem: Minimum Average Difference - https://leetcode.com/problems/minimum-average-difference/

class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        n = len(nums)
        total = sum(nums)
        prefix = 0
        
        min_diff = float('inf')
        min_index = -1
        
        for i in range(n):
            prefix += nums[i]
            left_avg = prefix // (i+1)
            
            if i == n-1:
                right_avg = 0
            else:
                right_avg = (total - prefix) // (n - i - 1)
            
            diff = abs(left_avg - right_avg)
            
            if diff < min_diff:
                min_diff = diff
                min_index = i
        
        return min_index
