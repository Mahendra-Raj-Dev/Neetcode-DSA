# Problem: Word Search II
# Pattern: trie + backtracking (DFS on grid)
# Idea:
# - Build a Trie from given words
# - DFS from each cell, following Trie paths
# - Add word when endOfWord is reached and prune to avoid duplicates
# Time: O(R * C * 4^L) worst case
# Space: O(N * L) for Trie + O(L) recursion stack

class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        ROWS, COLS = len(board), len(board[0])
        res = []
        path = set()

        self.root = TrieNode()
        cur = self.root
        for word in words:
            cur = self.root
            for c in word:
                if c not in cur.children:
                    cur.children[c] = TrieNode()
                cur = cur.children[c]
            cur.endOfWord = True
        
        
        def backtrack(r, c, word, cur):
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or (r, c) in path:
                return 
            char = board[r][c]
            if char not in cur.children:
                return 
            word.append(char)
            path.add((r, c))
            cur = cur.children[char]
            if cur.endOfWord:
                res.append("".join(word))
                cur.endOfWord = False
            
            backtrack(r, c+1, word, cur)
            backtrack(r, c - 1, word, cur)
            backtrack(r + 1, c, word, cur)
            backtrack(r - 1, c, word, cur)

            word.pop()
            path.remove((r, c))

        
        for r in range(ROWS):
            for c in range(COLS):
                backtrack(r, c, [], self.root)
        
        return res