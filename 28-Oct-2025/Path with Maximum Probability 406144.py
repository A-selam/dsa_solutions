# Problem: Path with Maximum Probability - https://leetcode.com/problems/path-with-maximum-probability/

class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        graph = defaultdict(list)
        for i, (a, b) in enumerate(edges):
            graph[a].append((b, succProb[i]))
            graph[b].append((a, succProb[i]))
        
        probs = [0.0] * n
        probs[start_node] = 1.0
        heap = [(-1.0, start_node)] 
        
        while heap:
            currProb, node = heappop(heap)
            currProb = -currProb  
            
            if node == end_node:
                return currProb  
            
            for nei, p in graph[node]:
                newProb = currProb * p
                if newProb > probs[nei]:
                    probs[nei] = newProb
                    heappush(heap, (-newProb, nei))
        
        return 0.0
