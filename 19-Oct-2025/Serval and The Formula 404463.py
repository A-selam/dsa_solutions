# Problem: Serval and The Formula - https://codeforces.com/problemset/problem/2085/C

def solve():
    x, y = map(int, input().split())

    if x == y:
        print(-1)
        return

    if x & y == 0:
        print(0)
        return
    
    k = 2 ** max(x, y).bit_length()
    k -= max(x, y)

    print(k)

t = int(input())
for _ in range(t):
    solve()