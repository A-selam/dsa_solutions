# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        memo = {}
        def rec(root):
            if root == None:
                return 0
            
            if root in memo:
                return memo[root]

            temp1 = root.val
            temp2 = 0

            if root.left:
                temp1 += rec(root.left.left) + rec(root.left.right)
                temp2 += rec(root.left)
            if root.right:
                temp1 += rec(root.right.left) + rec(root.right.right)
                temp2 += rec(root.right)
            
            memo[root] = max(temp1, temp2)
            return memo[root]
        
        return rec(root)        