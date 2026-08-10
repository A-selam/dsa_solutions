class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        ans = []
        q = deque()
        l = 0

        for r in range(k):
            while q and q[-1] < nums[r]:
                q.pop()
            q.append(nums[r])

        ans.append(q[0])
        
        for r in range(k, n):
            if nums[l] == q[0]:
                q.popleft()

            while q and q[-1] < nums[r]:
                q.pop()
            
            l += 1
            q.append(nums[r])

            ans.append(q[0])

        return ans