# Problem: Longest Palindromic Substring
# Pattern: two pointers (expand around center)
# Approach:
# - Treat each index as the center of a palindrome
# - Expand outward for both odd and even length palindromes
# - Update the longest palindrome found during expansion
# Time complexity: O(N^2), where N is length of string
# Space complexity: O(1)

class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        resLen = 0

        for i in range(len(s)):
            # odd
            l = r = i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    res = s[l: r+1]
                    resLen = (r - l + 1)
                l -= 1
                r += 1
            
            # even
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    res = s[l: r+1]
                    resLen = (r - l + 1)
                l -= 1
                r += 1
        return res