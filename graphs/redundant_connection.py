# Problem: Redundant Connection
# Pattern: union find (disjoint set)
# Approach:
# - Initialize each node as its own parent
# - Use path compression in find() for faster lookups
# - Use union by rank to attach smaller tree under larger tree
# - If two nodes already share the same parent, that edge is redundant
# Time complexity: O(N * α(N)), where α is inverse Ackermann (almost constant)
# Space complexity: O(N)

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        N = len(edges)
        par = [i for i in range(N + 1)]
        rank = [1] * (N+1)

        def find(n):
            p = par[n]
            while p != par[p]:
                par[p] = par[par[p]]
                p = par[p]
            
            return p
        
        def union(n1, n2):
            p1, p2 = find(n1), find(n2)

            if p1 == p2:
                return False
            
            if rank[p1] > rank[p2]:
                par[p2] = p1
                rank[p1] += rank[p2]
            else:
                par[p1] = p2
                rank[p2] += rank[p1]
            return True
        
        for n1, n2 in edges:
            if not union(n1, n2):
                return [n1, n2]