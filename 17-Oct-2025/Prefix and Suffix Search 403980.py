# Problem: Prefix and Suffix Search - https://leetcode.com/problems/prefix-and-suffix-search/

class TrieNode:
    def __init__(self):
        # self.children = [ None for _ in range(26) ]
        self.children = {}
        self.index = -1

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, idx: int, word: str) -> None:
        for i in range(len(word)):
            curr = self.root
            newWord = word + "|" + word
            for char in newWord[i:]:
                # print(newWord[i:])
                # temp = ord(char) - 97
                if char not in curr.children:
                    curr.children[char] = TrieNode()
                curr.children[char].index = idx
                curr = curr.children[char]

    def search(self, word: str):
        curr = self.root
        for char in word:
            # temp = ord(char)-97
            if char not in curr.children:
                return -1
            curr = curr.children[char]
        return curr.index

class WordFilter:

    def __init__(self, words: List[str]):
        self.Trie = Trie()
        for i, word in enumerate(words):
            self.Trie.insert(i, word)

    def f(self, pref: str, suff: str) -> int:
        ans = self.Trie.search(suff + "|" + pref)
        
        return (ans)


# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(pref,suff)