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

    def search(self, word: str) -> int:
        curr = self.root
        for i,char in enumerate(word):
            temp = ord(char)-97
            if curr.children[temp] == None:
                break
            curr = curr.children[temp]
            if curr.is_end:
                return i
        return -1

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for char in prefix:
            temp = ord(char)-97
            if curr.children[temp] == None:
                return False
            curr = curr.children[temp]
        return True

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        ans = []
        trie = Trie()
        for word in dictionary:
            trie.insert(word)

        words = sentence.split()
        for word in words:
            idx = trie.search(word)
            if idx == -1:
                ans.append(word)
                continue
            ans.append(word[:idx+1])
        
        return " ".join(ans)