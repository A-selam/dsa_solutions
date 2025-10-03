class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        n, m = len(heightMap), len(heightMap[0])
        visited = [[False] * m for _ in range(n)]
        heap = []

        for i in range(n):
            for j in range(m):
                if i in [0, n-1] or j in [0, m-1]:
                    heapq.heappush(heap, (heightMap[i][j], i, j))
                    visited[i][j] = True

        water = 0
        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        while heap:
            h, i, j = heapq.heappop(heap)
            for di, dj in directions:
                ni, nj = i + di, j + dj
                if 0 <= ni < n and 0 <= nj < m and not visited[ni][nj]:
                    visited[ni][nj] = True
                    nh = heightMap[ni][nj]
                    if nh < h:
                        water += h - nh
                    heapq.heappush(heap, (max(h, nh), ni, nj))

        return water