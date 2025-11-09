# Problem: Second Minimum Time to Reach Destination - https://leetcode.com/problems/second-minimum-time-to-reach-destination/

class Solution: 
    def secondMinimum(self, n: int, edges: List[List[int]], time: int, change: int) -> int:
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        def bfs_distance2(graph, start, target):
            distances1 = [-1] * (n + 1)
            distances2 = [-1] * (n + 1)
            distances1[start] = 0

            q = deque([(start, 0)]) 

            while q:
                curr, curr_time = q.popleft()

                if (curr_time // change) % 2 == 1:
                    curr_time += change - (curr_time % change)

                next_time = curr_time + time

                for neighbor in graph[curr]:
                    if distances1[neighbor] == -1:
                        distances1[neighbor] = next_time
                        q.append((neighbor, next_time))
                    elif distances2[neighbor] == -1 and distances1[neighbor] != next_time:
                        distances2[neighbor] = next_time
                        if neighbor == target:
                            return next_time
                        q.append((neighbor, next_time))

        return bfs_distance2(graph, 1, n)
