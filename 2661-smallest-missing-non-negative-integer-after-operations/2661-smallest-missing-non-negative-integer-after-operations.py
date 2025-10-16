class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        n = len(nums)
        count = defaultdict(int)

        for i, num in enumerate(nums):
            if nums[i] < 0:
                temp = math.ceil((-nums[i]) / value)
                nums[i] += (temp*value)
            
            temp = nums[i] // value
            temp2 = nums[i] - (temp*value)
            
            temp3 = 0
            if count[temp2] != 0:
                temp3 = count[temp2] * value
                count[temp2] += 1

            nums[i] = temp2 + temp3
            count[nums[i]] += 1
        
        nums.sort()
        
        ans = 0
        for num in nums:
            if num == ans:
                ans += 1

        return ans