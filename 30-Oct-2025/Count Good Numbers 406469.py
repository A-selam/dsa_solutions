# Problem: Count Good Numbers - https://leetcode.com/problems/count-good-numbers/

class Solution:
    def countGoodNumbers(self, n: int) -> int:
        evens = (n+1)//2
        odds = n - evens
        def exponentiation(base, power):
            base = 1
        return (pow(5, evens, ((10**9)+7)) * pow(4, odds, ((10**9)+7))) % ((10**9)+7)