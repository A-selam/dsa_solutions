# Problem: D - Knapsack 1 - https://atcoder.jp/contests/dp/tasks/dp_d

def solve():
    n, W = map(int, input().split())
    items = []
    for _ in range(n):
        w, v = map(int, input().split())
        items.append((w, v))

    memo = [0] * (W+1)

    for weight, value in items:
        for w in range(W, weight-1, -1):   
            memo[w] = max(memo[w], value + memo[w-weight])
    
    # for w in range(W+1):
    #     for item in items:
    #         if w >= item[0]:
    #             memo[w] = max(memo[w], item[1]+memo[w-item[0]])

    # print(memo)
    print(memo[W])
solve()