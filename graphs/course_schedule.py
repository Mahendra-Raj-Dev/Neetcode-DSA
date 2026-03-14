# Problem: Course Schedule
# Pattern: graph traversal (DFS with cycle detection)
# Approach:
# - Build an adjacency list where each course points to its prerequisites
# - Use DFS to check if a course leads to a cycle
# - Track the current DFS path using a visited set to detect cycles
# - If a cycle is found, it is impossible to finish all courses
# - After verifying a course, mark it as completed by clearing its prerequisites
# Time complexity: O(V + E), where V is number of courses and E is prerequisites
# Space complexity: O(V + E)

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {i: [] for i in range(numCourses)}
        visited = set()

        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        
        def dfs(crs):
            if crs in visited: return False

            if preMap[crs] == []: return True

            visited.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre): return False
            visited.remove(crs)
            preMap[crs] = []
            return True
        
        for crs in range(numCourses):
            if not dfs(crs): return False
        return True
