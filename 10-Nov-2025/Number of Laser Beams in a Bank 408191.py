# Problem: Number of Laser Beams in a Bank - https://leetcode.com/problems/number-of-laser-beams-in-a-bank/

class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        ans = 0
        prev = 0
        for num in bank:
            num = num.count('1')
            if num == 0:
                continue
            ans += prev*num
            prev = num 
        return ans