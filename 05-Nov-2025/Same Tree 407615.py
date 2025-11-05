# Problem: Same Tree - https://leetcode.com/problems/same-tree/description/

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def dfs(root):
            if not root:
                return ["#"]  
            return [root.val] + dfs(root.left) + dfs(root.right)
        
        return dfs(p) == dfs(q)
