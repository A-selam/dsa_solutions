class Solution:
    def minWindow(self, s: str, t: str) -> str:
        m = len(s)
        n = len(t)

        count_t = defaultdict(int)
        for char in t:
            count_t[char] += 1
        
        count_s = defaultdict(int)
        rem = sum(count_t.values())
        left = -1

        ans = (0, 0, float('inf'))

        for right, val in enumerate(s):
            if left == -1 and val not in count_t:
                continue
            
            if val in count_t:
                if left == -1:
                    left = right
                count_s[val] += 1
                if count_s[val] <= count_t[val]:
                    rem -= 1   

            while (
                    s[left] not in count_t or
                    count_s[s[left]] > count_t[s[left]]
                ):
                if s[left] not in count_t:
                    left += 1
                elif count_s[s[left]] > count_t[s[left]]:
                    count_s[s[left]] -= 1
                    left += 1
                elif count_t[s[left]] == count_s[s[left]]:
                    if s[left] in count_t:
                        break
                else:
                    count_s[s[left]] -= 1
                    rem += 1
                    break
            
            if rem == 0 and ans[2] > (right-left+1):
                ans = (left, right, right-left+1)
    
        if ans[2] != float("inf"):
            return s[ans[0]:ans[1]+1]
        return ""