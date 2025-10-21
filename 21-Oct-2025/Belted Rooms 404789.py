# Problem: Belted Rooms - https://codeforces.com/problemset/problem/1428/B

def solve():
    n = int(input())
    belts = input()

    if ">" not in belts or "<" not in belts:
        print(n)
        return 
    
    nodes = set()
    for i, char in enumerate(belts):
        if char == "-":
            nodes.add(i)
            nodes.add((i + 1) % n)
    
    print(len(nodes))

t = int(input())
for _ in range(t):
    solve()