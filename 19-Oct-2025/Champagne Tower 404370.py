# Problem: Champagne Tower - https://leetcode.com/problems/champagne-tower/

class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        prev = [poured]

        for row in range(1, query_row+1):
            temp = [0] * (row+1)
            for col in range(row+1):
                val1 = 0
                if col > 0 and prev[col-1] > 1:
                    val1 = prev[col-1] - 1

                val2 = 0
                if col <= row-1 and prev[col] > 1:
                    val2 = prev[col] - 1
                
                temp[col] += (val1 / 2) + (val2 / 2)
            
            prev = temp[:]
            
        return min(1, prev[query_glass])