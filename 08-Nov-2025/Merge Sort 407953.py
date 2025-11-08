# Problem: Merge Sort - https://codeforces.com/problemset/problem/873/D


def solve():
    n, k = map(int, input().split())

    if k % 2 == 0 or k > 2 * n - 1:
        print(-1)
        return

    splits = (k - 1) // 2

    nums = [i for i in range(n, 0, -1)] 
    collection = []
    count = [splits]

    def divide(a):
        if len(a) == 1:
            collection.append(a[0])
            return
        if count[0] == 0:
            collection.extend(sorted(a))
            return

        mid = (len(a)) // 2  
        count[0] -= 1
        divide(a[:mid])
        divide(a[mid:])

    divide(nums)
    print(*collection)

solve()