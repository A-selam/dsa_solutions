# Problem: A - Frog 1 - https://atcoder.jp/contests/dp/tasks/dp_a

import threading
from sys import stdin, stdout, setrecursionlimit

setrecursionlimit(1 << 30)
threading.stack_size(1 << 27)

def solve():
    m = int(input())
    h = list(map(int, input().split()))
    memo = {}
    memo[0] = 0
    memo[1] = abs(h[0] - h[1]) 

    for n in range(2, m):
        memo[n] = min(abs(h[n] - h[n-1]) + memo[n-1], abs(h[n] - h[n-2]) + memo[n-2])
    
    print(memo[m-1])

solve()