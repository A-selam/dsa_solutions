# Problem: Construct Quad Tree - https://leetcode.com/problems/construct-quad-tree/description/

"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        def divide(arr):
            if len(arr) == 1:
                return Node(arr[0][0], 1, None, None, None, None)
            
            check = arr[0][0]
            flag = True
            for row in arr:
                for num in row:
                    if num != check:
                        flag = False
            if flag:
                return Node(check, 1, None, None, None, None)
            
            mid = len(arr) // 2
            classes = defaultdict(list)
            for i in range(len(arr)):
                classes[i//mid].append(arr[i][:mid])
                classes[(i//mid)+2].append(arr[i][mid:])
            

            topLeft = divide(classes[0])
            topRight = divide(classes[2])
            bottomLeft = divide(classes[1])
            bottomRight = divide(classes[3])
            
            return Node(1, 0, topLeft, topRight, bottomLeft, bottomRight)
        
        graph = divide(grid)

        return graph