# Problem: Dreamoon and Stairs - https://codeforces.com/problemset/problem/476/A

def solve():
    n, m = map(int, input().split())
    temp = (n+1) // 2

    temp2 = temp % m
    if temp2 == 0:
        temp2 = m
    print(temp + (m-temp2) if temp + (m-temp2) <= n else -1 )
solve()