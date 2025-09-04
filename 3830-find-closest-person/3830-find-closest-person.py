class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        dif1 = abs(x-z)
        dif2 = abs(y-z)
        
        if dif1 < dif2:
            return 1
        elif dif1 > dif2:
            return 2
        else: 
            return 0