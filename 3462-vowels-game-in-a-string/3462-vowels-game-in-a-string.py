class Solution:
    def doesAliceWin(self, s: str) -> bool:
        count = 0
        vowels = set(["a", 'e', 'i', 'o', 'u'])
        for char in s:
            if char in vowels:
                count += 1
        if count == 0:
            return False
        else:
            return True
