# Problem: Petya and Strings - https://codeforces.com/problemset/problem/112/A

def string_comparison():
    s1 = input().lower()
    s2 = input().lower()

    if s1 > s2: print(1)
    if s1 < s2: print(-1)
    if s1 == s2: print(0)

    # l = len(s1)

    # state = 0
    # for i in range(l):
    #     if s1[i] > s2[i]:
    #         state = 1
    #     elif s1[i] < s2[i]:
    #         state = -1
    # print(state)
string_comparison()