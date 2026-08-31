class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        sl, fa = 0, 0

        while True:
            sl = nums[sl]
            fa = nums[nums[fa]]
            if sl == fa:
                break
        
        sl2 = 0
        while True:
            sl = nums[sl]
            sl2 = nums[sl2]
            if sl == sl2:
                break

        return sl
