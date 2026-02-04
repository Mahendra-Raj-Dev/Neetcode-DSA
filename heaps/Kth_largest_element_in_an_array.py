# Problem: Kth Largest Element in an Array
# Pattern: heap (min-heap of size k)
# Approach:
# - Maintain a min-heap of size k
# - Push elements into the heap and remove the smallest when size exceeds k
# - The top of the heap represents the k-th largest element
# Time complexity: O(N log K), where N is the number of elements
# Space complexity: O(K)

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []

        for n in nums:
            heapq.heappush(heap, n)
            if len(heap) > k:
                heapq.heappop(heap)
        
        return heap[0]