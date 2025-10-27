# Problem: A. Beautiful Matrix - https://codeforces.com/problemset/problem/263/A

def solve():
    mat = [list(map(int, input().split())) for _ in range(5)]
    
    ans = 0
    for i in range(5):
        for j in range(5):
            if mat[i][j] == 1:
                ans += abs(2-i) + abs(2-j)
    
    print(ans)
solve()