# Problem: Koko Eating Bananas
# Pattern: binary search (answer space)
# Approach:
# - Binary search on possible eating speeds
# - For each speed, calculate total hours required
# - Adjust search space based on feasibility
# Time complexity: O(N log M), where N is number of piles and M is max pile size
# Space complexity: O(1)

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l,r = 1,max(piles)
        res = r
        while l <= r:
            k = (l+r)//2
            hours = 0
            for p in piles:
                hours += math.ceil(p/k)

            if hours <= h:
                res = k
                r = k-1
            else:
                l = k+1 
        return res