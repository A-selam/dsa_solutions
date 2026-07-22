class Solution:
    def oneEmpty(self, nums):
        m = len(nums)
        if m % 2 == 0:
            temp = m // 2
            return (nums[temp] + nums[temp - 1]) / 2
        else:
            return nums[m // 2]

    def calculator(self, searched, determined, total):
        n, m = len(searched), len(determined)
        tot_l = (total + 1) // 2
        l, r = 0, n

        while l <= r:
            mid = (l + r) // 2

            s_left = mid
            d_left = tot_l - s_left

            s_l_g = float("-inf") if s_left == 0 else searched[s_left - 1]
            s_r_l = float("inf") if s_left == n else searched[s_left]

            d_l_g = float("-inf") if d_left == 0 else determined[d_left - 1]
            d_r_l = float("inf") if d_left == m else determined[d_left]

            if s_l_g <= d_r_l and d_l_g <= s_r_l:
                if total % 2 == 0:
                    return (max(s_l_g, d_l_g) + min(s_r_l, d_r_l)) / 2
                return max(s_l_g, d_l_g)

            if s_r_l < d_l_g:
                l = mid + 1
            else:
                r = mid - 1

    def findMedianSortedArrays(self, nums1, nums2):
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        if not nums1:
            return self.oneEmpty(nums2)

        return self.calculator(nums1, nums2, len(nums1) + len(nums2))