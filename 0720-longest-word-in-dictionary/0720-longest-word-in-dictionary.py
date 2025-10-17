class TrieNode:
    def __init__(self):
        self.children = {}

class Trie:
    def __init__(self):
        self.root = TrieNode()
    def insert(self, word):
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
    def search(self, prefix):
        curr = self.root
        for char in prefix:
            if char not in curr.children:
                return False
            curr = curr.children[char]
        return True
class Solution:
    def longestWord(self, words: List[str]) -> str:
        ans = ""
        trie = Trie()
        words.sort()
        for word in words:
            if len(word) == 1:
                trie.insert(word)
                ans = word if len(word) > len(ans) else ans
                continue
            if trie.search(word[:-1]):
                trie.insert(word)
                ans = word if len(word) > len(ans) else ans
        return ans