# Problem: Cheapest Flights Within K Stops
# Pattern: graph traversal (Bellman-Ford / shortest path)
# Approach:
# - Use Bellman-Ford relaxation for exactly k + 1 rounds
# - Copy the previous prices array each round to avoid extra stop usage
# - Relax all flight edges in each iteration
# - The final cost to destination after k + 1 rounds is the answer
# Time complexity: O((K + 1) * E), where E is number of flights
# Space complexity: O(N)

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        price = [float("inf")] * n
        price[src] = 0

        for i in range(k + 1):
            tempPrice = price[:]

            for s, d, p in flights:
                if price[s] == float("inf"):
                    continue
                if price[s] + p < tempPrice[d]:
                    tempPrice[d] = price[s] + p
            price = tempPrice
        
        return price[dst] if price[dst] != float("inf") else -1