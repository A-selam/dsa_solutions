class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        n = len(heights)
        m = len(heights[0])
        atDir = [(1, 0), (0, 1)]
        pacDir = [(-1, 0), (0, -1)]
        dir = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        def inBound(row, col):
            return 0 <= row < n and 0<= col < m

        def dfs_iterative(start):
            stack = [start]
            visited = set([start])
            pacFlag = False
            atFlag = False
            path = []

            while stack:
                row, col = stack.pop()
                # Do something with node
                
                if row == 0 or col == 0:
                    pacFlag = True
                if row == n-1 or col == m-1:
                    atFlag = True
                # print(row, col)
                # path.append((row, col))
                # check if pacific is reachable
                for r, c in dir:
                    newR = row + r
                    newC = col + c
                    if inBound(newR, newC) and (newR, newC) not in visited:
                        oldVal = heights[row][col]
                        newVal = heights[newR][newC]
                        if newVal <= oldVal:
                            # print(True)
                            stack.append((newR, newC))
                            visited.add((newR, newC))
                # print(stack)
            return pacFlag and atFlag
            # return path
        ans = []
        for i in range(n):
            for j in range(m):
                if dfs_iterative((i, j)):
                    ans.append([i, j])
        return ans