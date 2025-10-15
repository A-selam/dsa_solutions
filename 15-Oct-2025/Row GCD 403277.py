# Problem: Row GCD - https://codeforces.com/problemset/problem/1458/a

import math

def solve():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    ans = []
    prev = 0
    for i in range(n-1, 0, -1):
        prev = math.gcd(prev, a[i]-a[0])

    for num in b:
        temp = math.gcd(a[0]+num, prev)
        ans.append(temp)
    print(*ans)

solve()
        