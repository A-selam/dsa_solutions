# Problem: Find the City With the Smallest Number of Neighbors at a Threshold Distance - https://leetcode.com/problems/find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/

class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        dists = [[float('inf')] * n for _ in range(n)]
        
        for i in range(n):
            dists[i][i] = 0
        
        for f, t, w in edges:
            dists[f][t] = dists[t][f] = w
        
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    dists[i][j] = min(dists[i][j], dists[i][k] + dists[k][j])
        
        ans = (float('inf'), -1)
        for i in range(n):
            count = 0
            for j in range(n):
                if dists[i][j] <= distanceThreshold:
                    count += 1
            if count <= ans[0]:
                ans = (count, i)
        
        return ans[1]