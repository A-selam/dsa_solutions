# Problem: Minimum Cost to Convert String I - https://leetcode.com/problems/minimum-cost-to-convert-string-i/description/?envType=problem-list-v2&envId=shortest-path

class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        n = len(original)
        costs = [[float('inf')] * 26 for _ in range(26)]

        
        for i in range(26):
            costs[i][i] = 0

        for i in range(n):
            x = ord(original[i])-97
            y = ord(changed[i])-97
            z = cost[i]
            costs[x][y] = min(costs[x][y], z)

        for k in range(26):
            for i in range(26):
                for j in range(26):
                    costs[i][j] = min(costs[i][j], costs[i][k] + costs[k][j])
        
        ans = 0
        for i in range(len(source)):
            s, t = ord(source[i])-97, ord(target[i])-97
            temp = costs[(s)][(t)]
            if temp == float('inf'):
                return -1
            ans += temp
        
        return ans