class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        broken = set(brokenLetters)
        words = text.split()
        count = 0

        for word in words:
            is_valid = True
            for ch in word:
                if ch in broken:
                    is_valid = False
                    break
            if is_valid:
                count += 1

        return count
