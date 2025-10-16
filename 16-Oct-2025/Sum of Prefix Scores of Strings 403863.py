# Problem: Sum of Prefix Scores of Strings - https://leetcode.com/problems/sum-of-prefix-scores-of-strings/description/

class TrieNode:
    def __init__(self):
        self.is_end = False
        self.children = [None for _ in range(26)]
        self.score = 0

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        curr = self.root
        for char in word:
            temp = ord(char)-97
            if curr.children[temp] == None:
                curr.children[temp] = TrieNode()
            curr = curr.children[temp]
            curr.score += 1
        curr.is_end = True
    
    def calculateScore(self, word):
        score = 0
        curr = self.root
        for char in word:
            temp = ord(char)-97
            curr = curr.children[temp]
            score += curr.score
        return score

class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        trie = Trie()
        for word in words:
            trie.insert(word)
        
        ans = []
        for word in words:
            ans.append(trie.calculateScore(word))
        
        return ans