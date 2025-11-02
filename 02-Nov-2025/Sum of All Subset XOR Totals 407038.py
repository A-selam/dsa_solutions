# Problem: Sum of All Subset XOR Totals - https://leetcode.com/problems/sum-of-all-subset-xor-totals/

class Solution:
    def subsetXORSum(self, nums):
        subsets = []
        def backtrack(idx, subset):
            if idx == len(nums):
                subsets.append(subset[:])
                return

            subset.append(nums[idx])
            backtrack(idx + 1, subset)
            subset.pop()

            backtrack(idx + 1, subset)

        backtrack(0, [])

        res = 0
        for sub in subsets:
            total = 0
            for num in sub:
                total ^= num
            res += total

        return res