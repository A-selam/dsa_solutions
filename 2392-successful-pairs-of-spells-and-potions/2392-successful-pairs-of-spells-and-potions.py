class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        n, m = len(spells), len(potions)
        potions.sort()
        ans = [0] * n
        
        def bs(base):
            l, r = 0, m-1
            while l <= r:
                mid = (l+r) // 2
                if base * potions[mid] < success:
                    l = mid+1
                else: 
                    r = mid-1
            return l

        for i, num in enumerate(spells):
            ans[i] = m - bs(num)
        
        return ans