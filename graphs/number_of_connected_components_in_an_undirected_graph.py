# Problem: Number of Connected Components in an Undirected Graph
# Pattern: graph traversal (DFS)
# Approach:
# - Build an adjacency list for the graph
# - Iterate through all nodes
# - For each unvisited node, run DFS to mark all reachable nodes
# - Each DFS call represents one connected component
# Time complexity: O(V + E), where V is number of nodes and E is edges
# Space complexity: O(V + E)

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        count = 0
        preMap = {i: [] for i in range(n)}
        for node1, node2 in edges:
            preMap[node1].append(node2)
            preMap[node2].append(node1)
        
        visited = set()
        def dfs(child, parent):
            if child in visited:
                return
            visited.add(child)

            for c in preMap[child]:
                if c == parent:
                    continue
                dfs(c, child)
            
            return
        
        for child in range(n):
            if child in visited:
                continue
            count += 1
            dfs(child, -1)
        
        return count