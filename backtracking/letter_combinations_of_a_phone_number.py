# Problem: Letter Combinations of a Phone Number
# Pattern: Backtracking (DFS on digits)
# Idea:
# - Map each digit to its possible letters
# - Build combinations one character at a time
# - When length equals number of digits, save result
# - Backtrack after each choice
# Time: O(4^N)   (max 4 letters per digit)
# Space: O(N)    (recursion stack + current combination)

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits: return []
        res, sol = [], []
        num = [int(n) for n in digits]
        map_digits = {
            2: "abc",
            3: "def",
            4: "ghi",
            5: "jkl",
            6: "mno",
            7: "pqrs",
            8: "tuv",
            9: "wxyz"
        }

        def dfs(i):
            if len(sol) == len(num):
                res.append("".join(sol))
                return 
            
            for ch in (map_digits[num[i]]):
                sol.append(ch)
                dfs(i + 1)
                sol.pop()
        
        dfs(0)
        return res