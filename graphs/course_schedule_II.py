# Problem: Course Schedule II
# Pattern: graph traversal (DFS with topological sort)
# Approach:
# - Build an adjacency list mapping each course to its prerequisites
# - Use DFS to detect cycles and perform topological ordering
# - Use a cycle set to detect cycles in the current DFS path
# - Use a visited set to avoid reprocessing completed courses
# - Add courses to the result after all their prerequisites are processed
# Time complexity: O(V + E), where V is number of courses and E is prerequisites
# Space complexity: O(V + E)

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preMap = {i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        
        visited, cycle = set(), set()
        res = []
        def dfs(crs):
            if crs in cycle:
                return False
            
            if crs in visited:
                return True
            
            cycle.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False
            cycle.remove(crs)
            visited.add(crs)
            res.append(crs)
            return True
        
        for crs in range(numCourses):
            if not dfs(crs):
                return []
        
        return res