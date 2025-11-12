# Problem: Number of Parallelograms - https://codeforces.com/contest/660/problem/D

input = __import__('sys').stdin.readline
from collections import defaultdict
from math import comb

def solve():
    n = int(input())
    vers = []

    for _ in range(n):
        x, y = map(int, input().split())
        vers.append([x, y])
    
    midPoints = defaultdict(int)
    for p1 in range(len(vers)):
        x1, y1 = vers[p1]
        for p2 in range(p1+1, len(vers)):
            x2, y2 = vers[p2]
            midPoints[(x1 + x2, y1 + y2)] += 1
    
    ans = 0
    for count in midPoints:
        ans += comb(midPoints[count], 2)   
    
    print(ans)

solve()
