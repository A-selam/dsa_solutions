# Problem: Minimum Falling Path Sum - https://leetcode.com/problems/minimum-falling-path-sum/

class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        mat = [matrix[0][:] for _ in range(n)]

        for row in range(1, n):
            for col in range(n):
                mat[row][col] = matrix[row][col] + mat[row-1][col]
                if col != 0:
                    mat[row][col] = min(mat[row][col], matrix[row][col] + mat[row-1][col-1])
                if col != n-1:
                    mat[row][col] = min(mat[row][col], matrix[row][col] + mat[row-1][col+1])
        
        return min(mat[-1])