class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        prev, ans = 0, 0
        for bits in bank:
            count = 0
            for bit in bits:
                if bit == "1":
                    count += 1
            if count != 0:
                ans += prev * count
                prev = count
        return ans