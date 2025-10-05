class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        n = len(piles)
        l = 0
        r = n -1
        a, b = 0, 0
        flag = True
        while l < r:
            if piles[r] > piles[l]:
                if flag:
                    a += piles[r]
                else:
                    b += piles[r]
                r -= 1
            else:
                if flag:
                    a += piles[l]
                else:
                    b += piles[l]
                l += 1
        return a > b
