# Problem: Pacific Atlantic Water Flow - https://leetcode.com/problems/pacific-atlantic-water-flow

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        n = len(heights)
        m = len(heights[0])
        dir = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        def inBound(row, col):
            return 0 <= row < n and 0 <= col < m

        def dfs_iterative(start):
            stack = [start]
            visited = set([start])
            pacFlag = False
            atFlag = False

            while stack:
                row, col = stack.pop()
                
                if row == 0 or col == 0:
                    pacFlag = True
                if row == n-1 or col == m-1:
                    atFlag = True

                for r, c in dir:
                    newR = row + r
                    newC = col + c
                    if inBound(newR, newC) and (newR, newC) not in visited:
                        oldVal = heights[row][col]
                        newVal = heights[newR][newC]
                        if newVal <= oldVal:
                            
                            stack.append((newR, newC))
                            visited.add((newR, newC))
                
            return pacFlag and atFlag
    
        ans = []
        for i in range(n):
            for j in range(m):
                if dfs_iterative((i, j)):
                    ans.append([i, j])
        return ans