# Problem: Implement Trie (Prefix Tree)
# Pattern: trie (design / hashmap)
# Idea:
# - Each node stores children characters and end-of-word flag
# - Insert characters one by one into the trie
# - Search checks full word match
# - startsWith checks prefix existence
# Time:
# - insert: O(L)
# - search: O(L)
# - startsWith: O(L), where L is the length of the word
# Space: O(N * L), for storing all characters in the trie
class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False
class PrefixTree:

    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word: str) -> None:
        curr = self.root

        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.endOfWord = True

    def search(self, word: str) -> bool:
        curr = self.root

        for c in word:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        return curr.endOfWord


    def startsWith(self, prefix: str) -> bool:
        curr = self.root

        for c in prefix:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        return True
        