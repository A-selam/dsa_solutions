# Problem: Red and Blue - https://codeforces.com/contest/1469/problem/B

def solve():
    n = int(input())
    red = list(map(int, input().split()))
    m = int(input())
    blue = list(map(int, input().split()))

    ans = 0
    pre_red = [red[0]] * n
    pre_blu = [blue[0]] * m

    for i in range(1, n):
         pre_red[i] = red[i] + pre_red[i-1]
    for i in range(1, m):
         pre_blu[i] = blue[i] + pre_blu[i-1]

    ans = max(ans, max(pre_blu), max(pre_red))

    for k in pre_red:
        for l in pre_blu:
            ans = max(ans, k+l)
    print(ans)

t = int(input())
for _ in range(t):
    solve()