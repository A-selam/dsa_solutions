class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        total = numBottles
        while numBottles >= numExchange:
            empty = numBottles % numExchange
            x = numBottles // numExchange
            total += x
            numBottles = empty + x
        return total

