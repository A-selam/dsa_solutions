# Problem: B - Frog 2 - https://atcoder.jp/contests/dp/tasks/dp_b

from math import inf
def solve():
    n, k = map(int, input().split())
    h = list(map(int, input().split()))
    memo = {}
    memo[0] = 0  

    for i in range(1, n):
        memo[i] = inf
        for j in range(1, k + 1):
            if i - j >= 0:
                memo[i] = min(memo[i], abs(h[i] - h[i - j]) + memo[i - j])

    print(memo[n - 1])

solve()