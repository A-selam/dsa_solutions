# Problem: Find Original Array From Doubled Array (Optional) - https://leetcode.com/problems/find-original-array-from-doubled-array/

import collections 
class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        n = len(changed)
        changed.sort()

        counted = collections.Counter(changed)
        
        if n % 2 != 0:
            return []
        
        original = []
        for num in changed:
            if counted[num]%2 != 0 and num==0:
                return []
            if counted[num] == 0:
                continue
            if counted[num * 2] == 0:
                return []
            original.append(num)
            counted[num] -= 1        
            counted[num*2] -= 1  

        return original      