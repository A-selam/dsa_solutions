# Problem: Alien Dictionary - https://practice.geeksforgeeks.org/problems/alien-dictionary/1

from collections import defaultdict, deque

class Solution:
    def findOrder(self, words):
        graph = defaultdict(list)
        indegree = defaultdict(int)
        letters = set("".join(words))  
        
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            if len(w1) > len(w2) and w1.startswith(w2):
                return ""

            for j in range(min(len(w1), len(w2))):
                if w1[j] != w2[j]:
                    graph[w1[j]].append(w2[j])
                    indegree[w2[j]] += 1
                    break

        q = deque([ch for ch in letters if indegree[ch] == 0])
        order = []

        while q:
            ch = q.popleft()
            order.append(ch)
            for nei in graph[ch]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)

        if len(order) != len(letters):
            return ""

        return "".join(order)
