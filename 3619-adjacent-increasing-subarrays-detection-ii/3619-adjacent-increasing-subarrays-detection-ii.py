class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        leftCount = [1] * n
        rightCount = [1] * n

        for i in range(1, n):
            if nums[i] > nums[i-1]:
                leftCount[i] += leftCount[i-1]
        for i in range(n-2, -1, -1):
            if nums[i] < nums[i+1]:
                rightCount[i] += rightCount[i+1]
            
        ans = 0
        for i in range(n-1):
            ans = max(ans, min(leftCount[i], rightCount[i+1]))
    
        return ans