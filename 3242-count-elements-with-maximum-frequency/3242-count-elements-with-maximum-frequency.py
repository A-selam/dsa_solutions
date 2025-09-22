class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        counted = Counter(nums)
        max_freq = max(counted.values())
        ans = 0
        for num, freq in counted.items():
            if freq == max_freq:
                ans += 1
        
        return ans * max_freq