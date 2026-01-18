# Problem: Car Fleet
# Pattern: Stack / Monotonic Stack
# Approach:
# - Compute time for each car to reach the target
# - Sort cars by position in descending order
# - Iterate from closest to farthest and count fleets
# Time Complexity: O(n log n)
# Space Complexity: O(n)


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        time = []
        for i in range(len(position)):
            t = ((target - position[i])/speed[i])
            time.append((position[i], t))
        
        time.sort(reverse = True)

        fleet = 0
        curr_time = 0
        for p,t in time:
            if t > curr_time:
                fleet += 1
                curr_time = t
        
        return fleet