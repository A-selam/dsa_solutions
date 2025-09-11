class Solution:
    def sortVowels(self, s: str) -> str:
        s = list(s) 
        collected = []
        vowls = set(['a','e','i','o','u','A','E','I','O','U'])
        for i,char in enumerate(s):
            if char in vowls:
                collected.append(char)
                s[i] = ''
        collected.sort(reverse=True)

        for i, char in enumerate(s):
            if char == '':
                s[i] = collected.pop()
                
        return "".join(s)