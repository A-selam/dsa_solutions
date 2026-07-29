class Solution:
    def minWindow(self, s: str, t: str) -> str:
        original = Counter(t)
        window = defaultdict(int) 
        missing = len(t)

        ans_len = float('inf')
        ans = (0, 0)
        left = 0
        for right, ch in enumerate(s):
            if ch in original:
                window[ch] += 1
                if window[ch] <= original[ch]:
                    missing -= 1

            while missing == 0:
                if right - left + 1 < ans_len:
                    ans = (left, right)
                    ans_len = right-left+1
                
                if s[left] in original:
                    window[s[left]] -= 1
                    if window[s[left]] < original[s[left]]:
                        missing += 1
                left += 1
                        
        return (s[ans[0]:ans[1]+1]) if ans_len != float('inf') else ""