class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(dict)
        for (a,b), res in zip(equations, values):
            graph[a][b] = res
            graph[b][a] = 1/res
            
        def dfs(start, end, visited):
            if start not in graph or end not in graph:
                return -1.0
            if start == end:
                return 1.0

            visited.add(start)
            for nei, val in graph[start].items():
                if nei in visited:
                    continue
                temp = dfs(nei, end, visited)
                if temp != -1.0:
                    return temp * val
            return -1.0
        ans = []
        for a, b in queries:
            ans.append(dfs(a,b,set()))

        return ans