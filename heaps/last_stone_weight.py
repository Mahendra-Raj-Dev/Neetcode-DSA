# Problem: Last Stone Weight
# Pattern: heap (max-heap using min-heap)
# Approach:
# - Convert values to negative to simulate a max-heap
# - Repeatedly remove the two largest stones and push back their difference
# - Continue until one or no stone remains
# Time complexity: O(N log N), where N is the number of stones
# Space complexity: O(N)

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            y, x = -(heapq.heappop(stones)), -(heapq.heappop(stones))
            if y != x:
                heapq.heappush(stones, -(y-x))
        
        return -(stones[0]) if stones else 0