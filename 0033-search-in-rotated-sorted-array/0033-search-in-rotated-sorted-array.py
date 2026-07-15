class Solution:
    def binary(self, a, t):
        l = 0
        r = len(a)-1
        while l <= r:
            mid = (l + r) // 2
            if t == a[mid]:
                return mid
            if t < a[mid]:
                r = mid-1
            elif t > a[mid]:
                l = mid+1
        return -1

    def search(self, nums: List[int], target: int) -> int:
        idx = -1
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                idx = i+1

        if idx != -1:
            # p1 = nums[:idx]
            # p2 = nums[idx:]
            left = self.binary(nums[:idx], target)
            right = self.binary(nums[idx:], target)
            if right != -1:
                right += idx
                
            return max(left, right)
        else:
            # p1 = nums
            return self.binary(nums, target)
            
        