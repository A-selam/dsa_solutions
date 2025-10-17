# Problem: Minimum Integer - https://codeforces.com/problemset/problem/1101/A

def solve():
    l, r, d = map(int, input().split())
    if d < l or d > r:
        print(d)
        return
    
    temp = r // d
    print((temp + 1) * d)

t = int(input())
for _ in range(t):
    solve()