# Problem: Distribute Candies Among Children II - https://leetcode.com/problems/distribute-candies-among-children-ii/

class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        ans = 0
        if 3 * limit < n:
            return 0

        for i in range(min(limit, n)+1):
            left = max(0, n-i-limit)
            right = min(n-i, limit) + 1

            # print(i, (left, right), abs(right - left))
            
            ans += max(0, (right - left))
        return ans