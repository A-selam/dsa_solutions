class Solution:
    def maxOperations(self, s: str) -> int:
        n = len(s)
        prev = 0
        ans = 0
        for i in range(n-1, -1, -1):
            if s[i] == '1' and i != n-1:
                # print("in", i, s[i], s[i+1], prev, ans)
                if s[i+1] == '1':
                    ans += prev
                else:
                    prev += 1
                    ans += prev
                # print("out", prev, ans)
        return ans
