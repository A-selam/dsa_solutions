class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = defaultdict(int)
        l = 0

        count[s[l]] += 1
        ans = 1
        for r in range(1, len(s)):
            count[s[r]] += 1
            width = r - l + 1
            cur_max_count = max(count.values())

            while k < width - cur_max_count:
                count[s[l]] -= 1
                l += 1
                cur_max_count = max(count.values())
                width = r - l + 1
            
            ans = max(ans, width)
        
        return ans