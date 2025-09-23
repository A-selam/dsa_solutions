class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = list(map(int, version1.split('.')))
        v2 = list(map(int, version2.split('.')))

        n = len(v1)
        m = len(v2)
        if n > m:
            v2.extend([0]* (n-m))
        if n < m:
            v1.extend([0]* (m-n))
        
        for i in range(max(n,m)):
            if v1[i] > v2[i]: 
                return 1
            if v1[i] < v2[i]:
                return -1

        return 0