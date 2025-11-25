# Problem: Relative Sort Array
(Easy) - https://leetcode.com/problems/relative-sort-array/

class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        dic = defaultdict(int)
        for num in arr1:
            dic[num] += 1
        ans = []
        for num in arr2:
            temp = [num] * dic[num]
            dic[num] = 0
            ans.extend(temp)
        temp2 = []
        for el, val in dic.items():
            temp = [el] * val
            temp2.extend(temp)
        temp2.sort()
        ans.extend(temp2)
        return ans 