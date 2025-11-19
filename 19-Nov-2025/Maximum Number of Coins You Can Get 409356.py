# Problem: Maximum Number of Coins You Can Get - https://leetcode.com/problems/maximum-number-of-coins-you-can-get/

class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        n = len(piles)
        piles.sort()
        answer = 0
        print(piles)
        i = n//3
        while i < n:
            answer += (piles[i])
            i += 2
        return answer