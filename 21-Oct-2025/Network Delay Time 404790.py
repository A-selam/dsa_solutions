# Problem: Network Delay Time - https://leetcode.com/problems/network-delay-time/description/

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((w, v))
        
        heap = [(0, k)]
        heapq.heapify(heap)
        
        least = dict()
        
        while heap:
            time, node = heapq.heappop(heap)
            if node in least:
                continue
            least[node] = time
            for t, nei in graph[node]:
                if nei not in least:
                    heapq.heappush(heap, (time + t, nei))
        
        if len(least) != n:
            return -1
        return max(least.values())