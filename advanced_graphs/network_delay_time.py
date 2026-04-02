# Problem: Network Delay Time
# Pattern: graph traversal (Dijkstra / shortest path)
# Approach:
# - Build an adjacency list with (weight, neighbor)
# - Use a min-heap to always process the node with the smallest current distance
# - Skip already visited nodes
# - Track the maximum shortest distance among all reachable nodes
# Time complexity: O((V + E) log V), where V is nodes and E is edges
# Space complexity: O(V + E)

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges = defaultdict(list)
        for u, n1, w in times:
            edges[u].append((w, n1))
        
        minHeap = [(0, k)]
        visit = set()
        t = 0
        while minHeap:
            w1, n1 = heapq.heappop(minHeap)
            if n1 in visit:
                continue
            
            visit.add(n1)
            t = max(t, w1)

            for w2, n2 in edges[n1]:
                if n2 not in visit:
                    heapq.heappush(minHeap, (w1 + w2, n2))
        return t if len(visit) == n else -1



