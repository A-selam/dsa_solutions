# Problem: C - Vacation - https://atcoder.jp/contests/dp/tasks/dp_c

def solve():
    n = int(input())
    days = []
    for _ in range(n):
        days.append(list(map(int, input().split())))

    mat = [days[0][:] for _ in range(n)]
    for row in range(1, n):
        for task in range(3):
            mat[row][task] = 0
            for prevTask in range(3):
                if task != prevTask:
                    mat[row][task] = max(mat[row][task], mat[row-1][prevTask] + days[row][task])

    print(max(mat[-1]))