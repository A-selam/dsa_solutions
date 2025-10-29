# Problem: The Two Routes - https://codeforces.com/problemset/problem/601/A

from collections import defaultdict, deque

def bfs_distance(graph, start, target):
    q = deque([start])
    visited = set([start])
    distance = 0

    while q:
        for _ in range(len(q)):
            curr = q.popleft()
            if curr == target:
                return distance
            for neighbor in graph[curr]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    q.append(neighbor)
        distance += 1
    return -1

def solve():
    n, m = map(int, input().split())
    mapper_mat = [[0 for _ in range(n)] for _ in range(n)]

    railRoad = defaultdict(list)
    road = defaultdict(list)

    for _ in range(m):
        s, e = map(int, input().split())
        mapper_mat[s-1][e-1] = 1
        mapper_mat[e-1][s-1] = 1
    
    for i in range(n):
        for j in range(n):
            if i != j and mapper_mat[i][j] == 1:
                railRoad[i].append(j)
                railRoad[j].append(i)
            elif i != j and mapper_mat[i][j] == 0:
                road[i].append(j)
                road[j].append(i)
    
    distanceRoad = bfs_distance(road, 0, n-1)
    distanceRail = bfs_distance(railRoad, 0, n-1)
    if distanceRoad == -1 or distanceRail == -1:
        print(-1)
        return 
    print(max(distanceRoad, distanceRail))
solve()
