# Problem: Implement Trie (Prefix Tree) - https://leetcode.com/problems/implement-trie-prefix-tree/

class TrieNode:
        def __init__(self):
            self.is_end = False
            self.children = [ None for _ in range(26) ]

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for char in word:
            temp = ord(char) - 97
            if curr.children[temp] == None:
                curr.children[temp] = TrieNode()
            curr = curr.children[temp]
        curr.is_end = True 

    def search(self, word: str) -> bool:
        curr = self.root
        for char in word:
            temp = ord(char)-97
            if curr.children[temp] == None:
                return False
            curr = curr.children[temp]
        return curr.is_end

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for char in prefix:
            temp = ord(char)-97
            if curr.children[temp] == None:
                return False
            curr = curr.children[temp]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)