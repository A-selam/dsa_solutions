class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        target = num2.bit_count()
        curr = num1.bit_count()
        x = num1

        if curr > target:
            to_remove = curr - target
            for i in range(32):
                if to_remove == 0:
                    break
                if x & (1 << i): 
                    x &= ~(1 << i)
                    to_remove -= 1

        elif curr < target:
            to_add = target - curr
            for i in range(32):
                if to_add == 0:
                    break
                if not (x & (1 << i)):  
                    x |= (1 << i)  
                    to_add -= 1

        return x
