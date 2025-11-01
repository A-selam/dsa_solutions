# Problem: Selection of Personnel - https://codeforces.com/problemset/problem/630/F

import math
def solve():
    n = int(input())
    print(math.comb(n, 5) + math.comb(n, 6) + math.comb(n, 7))

solve()