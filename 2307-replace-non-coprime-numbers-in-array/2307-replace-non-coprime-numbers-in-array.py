class Solution:
    def replaceNonCoprimes(self, nums):
        stack = []
        
        for num in nums:
            stack.append(num)
            
            while len(stack) > 1:
                a, b = stack[-2], stack[-1]
                g = gcd(a, b)
                if g == 1: 
                    break
                
                lcm_val = a * b // g
                stack.pop()
                stack.pop()
                stack.append(lcm_val)
        
        return stack
