class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0

        count = defaultdict(int)

        left = 0
        ans = 1
        count[s[left]] += 1

        for right, cur in enumerate(s):
            if right == 0:
                continue
            count[cur] += 1
            
            while count[cur] > 1:
                count[s[left]] -= 1
                left += 1
            
            ans = max(ans, (right - left)+1)
        
        return ans
