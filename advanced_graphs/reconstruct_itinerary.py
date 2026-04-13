# Problem: Reconstruct Itinerary
# Pattern: graph traversal (DFS / Eulerian path)
# Approach:
# - Build adjacency list with destinations sorted in reverse lexical order
# - Use DFS to keep visiting the next smallest destination
# - Add airports to result only after exploring all outgoing edges
# - Reverse the result at the end to get the correct itinerary
# Time complexity: O(E log E), where E is number of tickets
# Space complexity: O(E)

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = defaultdict(list)
        for scr, dest in sorted(tickets, reverse=True):
            adj[scr].append(dest)
        
        res = []
        def dfs(scr):
            while adj[scr]:
                dfs(adj[scr].pop())
            res.append(scr)
        dfs("JFK")
        return res[::-1]