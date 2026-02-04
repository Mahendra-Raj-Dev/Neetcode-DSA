# Problem: K Closest Points to Origin
# Pattern: heap (max-heap of size k)
# Approach:
# - Compute distance of each point from origin
# - Maintain a max-heap of size k using negative distances
# - Remove farthest point when heap size exceeds k
# Time complexity: O(N log K), where N is the number of points
# Space complexity: O(K)

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        maxHeap = []
        for x, y in points:
            D = x**2 + y**2 # D**2 = x**2 + y**2
            heapq.heappush(maxHeap, (-D, [x, y]))
            if len(maxHeap) > k:
                heapq.heappop(maxHeap)
        
        return [point for D, point in maxHeap]