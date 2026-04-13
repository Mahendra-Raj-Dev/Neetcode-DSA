# Problem: Min Cost to Connect All Points
# Pattern: graph traversal (MST / Prim's algorithm)
# Approach:
# - Build adjacency list with Manhattan distance as edge cost
# - Use a min-heap to always pick the minimum cost edge
# - Expand the MST by adding the cheapest unvisited point
# - Continue until all points are connected
# Time complexity: O(N^2 log N), where N is number of points
# Space complexity: O(N^2)

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        N = len(points)
        adj = {i:[] for i in range(N)} # i: [cost, point]

        for i in range(N):
            x1, y1 = points[i]
            for j in range(i+1, N):
                x2, y2 = points[j]
                dist = abs(x1 - x2) + abs(y1 - y2)
                adj[i].append([dist, j])
                adj[j].append([dist, i])

        res = 0
        visit = set()
        minHeap = [[0, 0]]
        while len(visit) < N:
            cost, i = heapq.heappop(minHeap)
            if i in visit:
                continue
            res += cost
            visit.add(i)

            for neiCost, nei in adj[i]:
                if nei in visit:
                    continue
                heapq.heappush(minHeap, [neiCost, nei])
        return res