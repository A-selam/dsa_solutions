# Problem: Create Sorted Array through Instructions - https://leetcode.com/problems/create-sorted-array-through-instructions/

class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:
        MOD = 10**9 + 7
        cost = 0
        arr = SortedList()

        for num in instructions:
            left = arr.bisect_left(num) 
            right = len(arr) - arr.bisect_right(num) 
            cost = (cost + min(left, right)) % MOD
            arr.add(num)  
        return cost % MOD
