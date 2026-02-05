# Problem: Task Scheduler
# Pattern: heap + queue (greedy)
# Approach:
# - Use a max-heap to always pick the task with highest frequency
# - Use a queue to store tasks during their cooling period
# - Simulate time and schedule tasks while respecting the cooldown constraint
# Time complexity: O(N), where N is the number of tasks
# Space complexity: O(N)

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        maxHeap = [-c for c in count.values()]
        heapq.heapify(maxHeap)
        q = deque()

        time = 0
        while maxHeap or q:
            time += 1

            if not maxHeap:
                time = q[0][1]
            else:
                cnt = 1 + heapq.heappop(maxHeap)
                if cnt:
                    q.append([cnt, time + n])
            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])
        return time

