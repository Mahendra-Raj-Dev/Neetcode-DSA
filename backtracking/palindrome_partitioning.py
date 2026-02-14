# Problem: Palindrome Partitioning
# Pattern: Backtracking (DFS on string)
# Idea:
# - Start from index 0 and try all possible substrings
# - If substring s[i:j+1] is a palindrome, choose it
# - Recurse for the remaining string starting at j+1
# - Backtrack by removing the last chosen substring
# Time: O(N * 2^N)   (checking palindromes + exploring all partitions)
# Space: O(N)        (recursion stack + current partition path)

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res, part = [], []

        def dfs(i):
            if i == len(s):
                res.append(part[:])
                return 
            
            for j in range(i, len(s)):
                if self.ispali(s, i, j):
                    part.append(s[i: j+1])
                    dfs(j+1)
                    part.pop()
        dfs(0)
        return res
    
    def ispali(self, s, l, r):
        while l < r:
            if s[l] != s[r]:
                return False
            
            l, r = l+1, r-1
        return True