# Problem: Graph Valid Tree
# Pattern: graph traversal (DFS with cycle detection)
# Approach:
# - Build an adjacency list for the undirected graph
# - Use DFS to traverse nodes while tracking the parent node
# - If a visited node is reached again (not the parent), a cycle exists
# - After DFS, ensure all nodes were visited to confirm the graph is connected
# Time complexity: O(V + E), where V is number of nodes and E is edges
# Space complexity: O(V + E)

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        preMap = {i: [] for i in range(n)}

        for node1, node2 in edges:
            preMap[node1].append(node2)
            preMap[node2].append(node1)
        
        visited = set()
        def dfs(child, parent):
            if child in visited:
                return False
            
            visited.add(child)
            for c in preMap[child]:
                if c == parent:
                    continue
                
                if not dfs(c, child):
                    return False
            return True
        
        if not dfs(0, -1):
            return False
        
        return True if len(visited) == n else False