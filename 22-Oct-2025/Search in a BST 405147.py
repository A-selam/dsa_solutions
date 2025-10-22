# Problem: Search in a BST - https://leetcode.com/problems/search-in-a-binary-search-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def search(node, num):
            if not node:
                return 
            if num == node.val:
                return node
            if node.val > num:
                return search(node.left, num)
            if node.val < num:
                return search(node.right, num)
        return search(root, val)
