# Problem: Design Add and Search Words Data Structure
# Pattern: trie + DFS (design)
# Idea:
# - Store words in a Trie structure
# - Use DFS to handle '.' wildcard during search
# - Explore all possible child paths when wildcard is encountered
# Time:
# - addWord: O(L)
# - search: O(L) in normal case, up to O(26^L) in worst case with wildcards
# Space: O(N * L), for storing all characters in the trie

class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root

        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.endOfWord = True

    def search(self, word: str) -> bool:
        def dfs(j, root):
            cur = root
            for i in range(j, len(word)):
                c = word[i]

                if c == ".":
                    for child in cur.children.values():
                        if dfs(i+1, child):
                            return True
                    return False
                else:
                    if c not in cur.children:
                        return False
                    cur = cur.children[c]
            return cur.endOfWord
        return dfs(0, self.root)