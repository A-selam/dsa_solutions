class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        stack = []
        ans = 0
        for i in range(len(colors)):
            if not stack or stack[-1][0] != colors[i]:
                stack.append((colors[i], neededTime[i]))
                continue
            if stack[-1][0] == colors[i]:
                if stack[-1][1] < neededTime[i]:
                    ans += stack[-1][1]
                    stack.pop()
                    stack.append((colors[i], neededTime[i]))
                else:
                    ans += neededTime[i]

        return ans