# Problem: Merge K Sorted Linked Lists
# Pattern: linked list
# Approach:
# - Use a min-heap (priority queue) to always extract the smallest node
# - Push the head of each list into the heap
# - Repeatedly pop the smallest element and push its next node 
# Time complexity: O(N log K), where N is the total number of nodes and K is the number of lists
# space complexity: O(K)

import heapq
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []

        for i, node in enumerate(lists):
            if node:
                heapq.heappush(heap, (node.val, i, node))
        D = ListNode()
        curr = D
        while heap:
            val, i, node = heapq.heappop(heap)
            curr.next = node
            curr = node
            node = node.next
            if node:
                heapq.heappush(heap, (node.val, i, node))
        
        return D.next