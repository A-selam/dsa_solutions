class Solution:
    def maxFreqSum(self, s: str) -> int:
        vowels = set(['a','e','i','o','u'])
        counted = Counter(s)
        consMax = 0
        vowMax = 0
        for char, count in counted.items():
            if char in vowels:
                vowMax = max(vowMax, count)
            else:
                consMax = max(consMax, count)
        return vowMax + consMax