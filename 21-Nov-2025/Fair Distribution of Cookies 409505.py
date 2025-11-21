# Problem: Fair Distribution of Cookies - https://leetcode.com/problems/fair-distribution-of-cookies/

class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        child = [0] * k
        self.ans = float('inf')

        def backtrack(i, max_so_far):
            if max_so_far >= self.ans:
                return
            if i >= len(cookies):
                self.ans = min(self.ans, max(child))
                return 
            
            for j in range(k):
                child[j] += cookies[i]
                backtrack(i + 1, max(max_so_far, child[j]))
                child[j] -= cookies[i]
        
        backtrack(0, 0)
        return self.ans