class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        memo = {}
        n = len(ring)
    
        def dp(tp, curr):
            if curr >= len(key):
                return 0
            
            state = (tp, curr)
            if state in memo:
                return memo[state]
            
            ops = 0
            i = tp
            while ring[i] != key[curr]:
                i = (i+1) % n
                ops += 1
            res = (ops+1) + dp(i, curr+1)

            ops = 0
            i = tp
            while ring[i] != key[curr]:
                i -= 1
                ops += 1
                if i < (0-n):
                    i = -1
            
            res = min(res, (ops+1) + dp(i, curr+1))
            memo[state] = res
            
            return res

        return dp(0, 0)