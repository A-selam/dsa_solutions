class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        left = 0
        right = n-1
        ans = 0
        while left < right:
            min_h = min(height[left], height[right])
            curr = (right-left)*min_h
            ans = max(ans, curr) 
            if height[left] < height[right]:
                left += 1
            else: 
                right -= 1
        return ans