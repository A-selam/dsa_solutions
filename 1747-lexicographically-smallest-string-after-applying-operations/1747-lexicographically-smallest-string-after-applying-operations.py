class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        n = len(s)
        ans = s
        stack = [s]
        vis = set([s])

        while stack:
            num = stack.pop()
            ans = min(ans, num)

            numL = list(num)
            for i in range(n):
                if i % 2 == 1:
                    numL[i] = str((int(numL[i]) + a) % 10)
                
            newNode = "".join(numL)
            if newNode not in vis:
                vis.add(newNode)
                stack.append(newNode)
            
            shifted = []
            for i in range(b, b+n):
                shifted.append(num[i%len(s)])
            
            newNode = "".join(shifted)
            if newNode not in vis:
                vis.add(newNode)
                stack.append(newNode)
        
        return ans