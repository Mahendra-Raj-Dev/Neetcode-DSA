# Problem: Kth Largest Element in a Stream
# Pattern: heap (min-heap)
# Approach:
# - Maintain a min-heap of size k
# - Push new elements and remove the smallest when size exceeds k
# - The top of the heap always represents the k-th largest element
# Time complexity: O(log K) per insertion
# Space complexity: O(K)

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.minHeap, self.k = nums, k
        heapq.heapify(self.minHeap)
        while len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)

    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val)
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
        return self.minHeap[0]
        
