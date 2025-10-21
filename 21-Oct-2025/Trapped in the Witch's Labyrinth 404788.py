# Problem: Trapped in the Witch's Labyrinth - https://codeforces.com/problemset/problem/2034/C

def solve():
    n, m = map(int, input().split())
    grid = [list(input()) for _ in range(n)]
    
    stack = []
    vis = set()

    for i in range(n):
        for j in range(m):
            if i == 0 and grid[i][j] == "U":
                stack.append((i, j))
                vis.add((i, j))
            if j == 0 and grid[i][j] == "L":
                stack.append((i, j))
                vis.add((i, j))
            if j == m - 1 and grid[i][j] == "R":
                stack.append((i, j))
                vis.add((i, j))
            if i == n - 1 and grid[i][j] == "D":
                stack.append((i, j))
                vis.add((i, j))

    dirs = {
        "U": (1, 0),
        "R": (0, -1),
        "D": (-1, 0),
        "L": (0, 1)
    }

    while stack:
        i, j = stack.pop()

        for d, dir in dirs.items():
            x, y = i + dir[0], j + dir[1]
            if 0 <= x < n and 0 <= y < m and (x, y) not in vis and grid[x][y] == d:
                vis.add((x, y))
                stack.append((x, y))
    
    invalid_count = len(vis)
    for i in range(n):
        for j in range(m):
            if grid[i][j] == "?":
                flag = False
                for dir in dirs.values():
                    x, y = i + dir[0], j + dir[1]
                    if 0 <= x < n and 0 <= y < m and (x, y) not in vis:
                        flag = True
                if not flag:
                    invalid_count += 1
    
    print(n *m - invalid_count)

t = int(input())
for _ in range(t):
    solve()