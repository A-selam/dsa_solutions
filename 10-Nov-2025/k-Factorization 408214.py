# Problem: k-Factorization - https://codeforces.com/problemset/problem/797/A

def solve():
    n, k = map(int, input().split())

    if k == 1:
        print(n)
        return 
    
    st = 2
    arr = []
    while n > 1:
        while n % st == 0:
            arr.append(st)
            n //= st
            # print(st, n)
            if len(arr) == k-1 and n > 1:
                arr.append(n)
                break

        if len(arr) == k:
            break
        st += 1
    
    if len(arr) == k:
        print(*arr)
    else:
        print(-1)

solve()
