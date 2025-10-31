# Problem: Number of Ways to Reach a Position After Exactly k Steps - https://leetcode.com/problems/number-of-ways-to-reach-a-position-after-exactly-k-steps/

class Solution:
    def numberOfWays(self, startPos: int, endPos: int, k: int) -> int:
        diff = endPos - startPos
        # print(k-diff)
        if (k-diff) % 2 == 1 or k-diff < 0:
            return 0
        return (math.comb(k, ((k-diff)//2))) % ((10**9)+7) 