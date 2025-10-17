# Problem: Bear and Poker - https://codeforces.com/problemset/problem/574/C

def solve():
    n = int(input())
    bids = list(map(int, input().split()))

    for i in range(n):
        while bids[i] % 2 == 0:
            bids[i] //= 2
        while bids[i] % 3 == 0:
            bids[i] //= 3
    
    for i in range(n):
        if bids[i] != bids[i-1]:
            print("No")
            return 
    print("Yes")

solve()