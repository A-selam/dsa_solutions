# Problem: Flipping an Image - https://leetcode.com/problems/flipping-an-image/description/

class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for row in image:
            for i in range(len(row)):
                if row[i] == 1:
                    row[i] = 0
                else:
                    row[i] = 1
            row.reverse()
        return image
        