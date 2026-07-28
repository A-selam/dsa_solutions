class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s1)
        if n > len(s2):
            return False

        count_s1 = defaultdict(int)
        for char in s1:
            count_s1[char] += 1

        count_s2 = defaultdict(int)
        l = 0

        for r in range(len(s2)):
            count_s2[s2[r]] += 1

            if r - l + 1 > n:
                count_s2[s2[l]] -= 1
                l += 1

            if r - l + 1 == n:
                f = True
                for char in count_s1:
                    if count_s1[char] != count_s2[char]:
                        f = False
                        break

                if f:
                    return True

        return False