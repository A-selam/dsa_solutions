# Problem: Arranging Coins - https://leetcode.com/problems/arranging-coins/description/

class Solution:
    def arrangeCoins(self, n: int) -> int:
        row = 1
        while n >= row:
            n -= row
            row += 1
        return row - 1
