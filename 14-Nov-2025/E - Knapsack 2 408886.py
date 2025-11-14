# Problem: E - Knapsack 2 - https://atcoder.jp/contests/dp/tasks/dp_e

import threading
from sys import stdin, stdout, setrecursionlimit

setrecursionlimit(1 << 30)
threading.stack_size(1 << 27)

n, W = map(int, input().split())
k = []
sum_ = 0
for i in range(n):
    k.append(list(map(int, stdin.readline().strip().split() )))
    sum_ += k[i][1]
memo = {}
dp = [[float("inf")]*(sum_ + 1) for _ in range(n+1)]
dp[0][0] = 0
# dp[0][k[0][1]] = k[0][0]
for i in range(1, n+1):
    w,v= k[i-1]
    for j in range(sum_+1):
        dp[i][j] = dp[i-1][j]
        if j >= v:
            dp[i][j]= min(dp[i][j], dp[i-1][j-v]+ w)
# print(dp)
for i in range(sum_,-1,-1):
    if W >= dp[n][i]:
        print(i)
        break