# Problem: Minimum Add To Make Parentheses Valid - https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/

class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []
        for char in s:
            if stack:
                if char == ")" and stack[-1] == '(':
                    stack.pop()
                    continue


            stack.append(char)

        return len(stack)