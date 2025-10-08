class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 1:
            return 0

        check = [True] * (n)
        check[0]= check[1] = False
        
        i = 2
        while i < n:
            if check[i]:
                j = i * i
                while j < n:
                    check[j] = False
                    j += i
            
            i += 1
        
        count = 0
        for flag in check:
            if flag:
                count += 1
                
        return count
