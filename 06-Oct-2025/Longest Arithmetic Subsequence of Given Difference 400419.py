# Problem: Longest Arithmetic Subsequence of Given Difference - https://leetcode.com/problems/longest-arithmetic-subsequence-of-given-difference/description/

class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        n = len(arr)
        memo = defaultdict(int)

        for num in arr:
            memo[num] = 1+memo[num-difference]
        
        return max(memo.values())

        # memo = {}
        # def dp(i):
        #     if i == n-1:
        #         return 0
        #     if i in memo:
        #         return memo[i]
            
        #     temp = 0
        #     for j in range(i+1, n):
        #         if arr[j]-arr[i] == difference:
        #             temp = max(temp, 1+dp(j))
        #     memo[i] = temp
        #     return temp

        ans = 0
        for i in range(n-1):
            ans = max(ans, dp(i))
        return ans+1