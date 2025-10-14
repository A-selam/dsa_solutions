class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        ab = lcm(a,b)
        ac = lcm(a,c)
        bc = lcm(b,c)
        abc = lcm(a,b,c)

        left = 1
        right = n*min(a,b,c)

        while left < right:
            mid = (left+right) // 2

            count = mid//a + mid//b + mid//c - mid//ab - mid//ac - mid//bc + mid//abc
            
            if count < n:
                left = mid+1
            else:
                right = mid
        
        return left 
        