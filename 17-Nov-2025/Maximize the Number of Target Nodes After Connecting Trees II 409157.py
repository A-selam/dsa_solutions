# Problem: Maximize the Number of Target Nodes After Connecting Trees II - https://leetcode.com/problems/maximize-the-number-of-target-nodes-after-connecting-trees-ii/

class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]]) -> List[int]:
        graph1 = defaultdict(list)
        for u, v in edges1:
            graph1[u].append(v)
            graph1[v].append(u)
        
        graph2 = defaultdict(list)
        for u, v in edges2:
            graph2[u].append(v)
            graph2[v].append(u)

        g1Level = defaultdict(int)
        g1NodeLevel = defaultdict(int)
        g2Level = defaultdict(int)
        g2NodeLevel = defaultdict(int)

        def bfs(start, graph, gLevel, gNodeLevel):
            q = deque([start])
            vis = set([start])
            level = 0

            while q:
                gLevel[level] += len(q)
                for _ in range(len(q)):
                    node = q.popleft()
                    gNodeLevel[node] = level
                    # do something here
                    for nei in graph[node]:
                        if nei not in vis:
                            q.append(nei)
                            vis.add(nei)
                level += 1
        bfs(0, graph1, g1Level, g1NodeLevel)
        bfs(0, graph2, g2Level, g2NodeLevel)

        g1Evens = 0
        g1Odds = 0
        for level, count in g1Level.items():
            if level % 2 == 0:
                g1Evens += count
            else:
                g1Odds += count
        g2Evens = 0
        g2Odds = 0
        for level, count in g2Level.items():
            if level % 2 == 0:
                g2Evens += count
            else:
                g2Odds += count
        
        ans = [0] * len(g1NodeLevel)
        for node, level in g1NodeLevel.items():
            temp = max(g2Evens, g2Odds)
            if level % 2 == 0:
                temp += g1Evens
            else:
                temp += g1Odds
            ans[node] = temp

        return ans