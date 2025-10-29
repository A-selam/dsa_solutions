# Problem: Vowels of All Substrings - https://leetcode.com/problems/vowels-of-all-substrings/

class Solution:
    def countVowels(self, word: str) -> int:
        n = len(word)
        pre = [0] * len(word)
        suf = [0] * len(word)
        vowels = set(["a", "e", "i", "o", "u"])

        for i in range(len(word)):
            if word[i] in vowels:
                pre[i] = (n - i)
        for i in range(n-1, -1, -1):
            if word[i] in vowels:
                suf[i] = i-0+1
        
        for i in range(n):
            pre[i] *= suf[i]
        
        return sum(pre)
