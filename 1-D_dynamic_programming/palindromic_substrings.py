# Problem: Palindromic Substrings
# Pattern: two pointers (expand around center)
# Approach:
# - Treat each index as the center of a palindrome
# - Expand outward for both odd and even length palindromes
# - Count every valid palindrome found during expansion
# Time complexity: O(N^2), where N is length of string
# Space complexity: O(1)

class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        
        for i in range(len(s)):
            # odd
            l = r = i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1
            
            # even
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1
        return res