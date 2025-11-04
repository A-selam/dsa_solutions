# Problem: Number of Pairs Satisfying Inequality - https://leetcode.com/problems/number-of-pairs-satisfying-inequality/

class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        temp = []
        for num1, num2 in zip(nums1, nums2):
            temp.append(num1-num2)
        # print(temp)
        def divide(arr, count):
            if len(arr) <= 1:
                # print("base", arr)
                return arr, 0
            
            mid = len(arr) // 2
            # print(arr, arr[:mid], arr[mid:])
            part1, c1 = divide(arr[:mid], count)
            part2, c2 = divide(arr[mid:], count)
            return merge(part1, part2, c1+c2)

        def merge(arr1, arr2, count):
            # print("merge", arr1, arr2, count)
            result = []
            i = j = 0
            n = len(arr2)
            temp = sorted(arr2)
            for num in arr1:
                # print(num-diff, temp, bisect_left(temp, (num-diff)), n - bisect_left(arr2, num-diff))
                count += n - bisect_left(temp, num-diff)
           
            # while i < len(arr1) and j < len(arr2):
            #     if arr1[i] <= arr2[j] + diff:
            #         count += 1
            #         j += 1
            #     else:
            #         i += 1
            # for num in arr1:
            #     for num2 in arr2:
                    # if num <= num2+diff:
            #             count += 1

            # print("merge result", arr1+arr2, count)
            return arr1+arr2, count 

        res, ans = divide(temp, 0)
        return ans