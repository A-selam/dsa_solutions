class TrieNode:
    def __init__(self):
        self.is_end = False
        self.children = [ None for _ in range(26) ]

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for char in word:
            temp = ord(char) - 97
            if curr.children[temp] == None:
                curr.children[temp] = TrieNode()
            curr = curr.children[temp]
        curr.is_end = True

    def search(self, word: str) -> bool:
        def dfs(node, idx):
            if node == None:
                return False
            if idx == len(word):
                return node.is_end

            if word[idx] == ".":
                for child in node.children:
                    if child != None:
                        if dfs(child, idx+1):
                            return True
                return False
            else:
                return dfs(node.children[ord(word[idx])-97], idx+1)
        
        return dfs(self.root, 0)




# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)