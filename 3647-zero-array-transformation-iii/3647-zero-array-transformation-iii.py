class Solution:
    def maxRemoval(self, nums: List[int], queries: List[List[int]]) -> int:
        n = len(nums)
        pre = [0] * (n+1)
        rs = 0
        heapify(queries)
        candidates = []

        for i in range(n):
            rs += pre[i]
            while queries and queries[0][0] <= i:
                left, right = heappop(queries)
                heappush(candidates, -right)
                
            while nums[i] + rs > 0:
                if not candidates or -candidates[0] < i:
                    return -1
                
                right = -heappop(candidates)
                rs -= 1
                pre[right+1] += 1

        return len(candidates)