# Problem: Find the Town Judge - https://leetcode.com/problems/find-the-town-judge/

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        degrees = [0] * n
        for tr in trust:
            degrees[tr[0]-1] -= 1
            degrees[tr[1]-1] += 1
        
        for i, degree in enumerate(degrees):
            if degree == n-1:
                return i+1

        return -1