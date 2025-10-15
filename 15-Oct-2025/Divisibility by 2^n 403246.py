# Problem: Divisibility by 2^n - https://codeforces.com/contest/1744/problem/D

def solve():
    n = int(input())
    nums = list(map(int, input().split()))

    def countTwos(x):
        count = 0
        while x % 2 == 0:
            count += 1
            x //= 2
        return count

    curr = 0
    for num in nums:
        curr += countTwos(num)
    
    if curr >= n:
        print(0)
        return 
    
    ops = 0
    new = []
    for i in range(n, 0, -1):
        temp = countTwos(i)
        if temp != 0:
            new.append(countTwos(i))
    
    new.sort(reverse=True)
    for val in new:
        curr += val
        ops += 1
        if curr >= n:
            print(ops)
            return
    
    print(-1)

t = int(input())
for _ in range(t):
    solve()