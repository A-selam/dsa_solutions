# Problem: Complicated GCD - https://codeforces.com/contest/664/problem/A

def solve():
    a, b = map(int, input().split())
    print(a if a == b else 1)

solve()