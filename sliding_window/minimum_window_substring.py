# Problem: Minimum Window Substring
# Pattern: Sliding Window
# Approach:
# - Maintain frequency count of characters in t
# - Expand right pointer to satisfy requirement
# - Shrink left pointer to minimize window
# Time Complexity: O(n)
# Space Complexity: O(m) where m = unique chars in t

class Solution(object):
    def minWindow(self, s, t):
        if t == "":
            return ""
        
        countT, window = {}, {}
        for c in t:
            countT[c] = countT.get(c, 0)+1
        
        have,need = 0,len(countT)
        res, reslen = [-1,-1], float("infinity")
        l = 0
        for r in range(len(s)):
            c = s[r]
            window[c] = window.get(c, 0)+1

            if c in countT and window[c] == countT[c]:
                have += 1
            
            while have == need:
                if (r-l+1) < reslen:
                    res = [l,r]
                    reslen = r-l+1
                
                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1

        l,r = res
        return s[l: r+1] if reslen != float("infinity") else "" 