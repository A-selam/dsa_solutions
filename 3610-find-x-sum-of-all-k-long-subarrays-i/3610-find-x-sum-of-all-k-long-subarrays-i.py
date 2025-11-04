class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        def x_sum(start):
            counted = Counter(nums[start:start+k])
            heap = []
            for key, val in counted.items():
                heappush(heap, (-val, -key))
            xsum = 0
            for _ in range(x):
                val, occ = heappop(heap)
                xsum += (val * occ)
                if not heap:
                    break
    
            return xsum
        ans = []
        for i in range(len(nums)-k+1):
            ans.append(x_sum(i))
        
        return ans