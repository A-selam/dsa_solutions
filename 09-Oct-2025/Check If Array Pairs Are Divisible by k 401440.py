# Problem: Check If Array Pairs Are Divisible by k - https://leetcode.com/problems/check-if-array-pairs-are-divisible-by-k/

class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        dic = defaultdict(int)
        for num in arr:
            temp = num % k
            if dic[k-temp] != 0:
                dic[k-temp] -= 1
            else:
                dic[temp] += 1
        
        for key, val in dic.items():
            if key == 0 and val%2 != 0:
                return False
            if key != 0 and val != 0:
                return False
        return True