# Problem: Dictionary - https://codeforces.com/problemset/problem/1674/B

def solve():
    word = input().strip()
    x = ord(word[0]) - 97
    y = ord(word[1]) - 97

    if y > x:
        ans = x * 25 + y
    else:
        ans = x * 25 + y + 1
    print(ans)  

t = int(input())
for _ in range(t):
    solve()
