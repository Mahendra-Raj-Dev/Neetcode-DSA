# Problem: Find Median from Data Stream
# Pattern: two heaps (design)
# Approach:
# - Use a max-heap for the lower half and a min-heap for the upper half
# - Balance the heaps so their sizes differ by at most one
# - Compute median based on the top elements of both heaps
# Time complexity:
# - addNum: O(log N)
# - findMedian: O(1)
# Space complexity: O(N)

class MedianFinder(object):

    def __init__(self):
        self.small = [] #Max heap
        self.large = [] #Min heap

    def addNum(self, num):
        if self.large and num > self.large[0]:
            heapq.heappush(self.large, num)
        else:
            heapq.heappush(self.small, -1 * num)

        if len(self.small) > len(self.large) + 1:
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        if len(self.large) > len(self.small) + 1:
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -1 * val)

    def findMedian(self):
        if len(self.small) > len(self.large):
            return -1 * self.small[0]
        elif len(self.large) > len(self.small):
            return self.large[0]
        return (-1 * self.small[0] + self.large[0]) / 2.0
