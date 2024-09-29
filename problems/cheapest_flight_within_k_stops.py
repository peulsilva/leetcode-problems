# https://leetcode.com/problems/cheapest-flights-within-k-stops/

from typing import List

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = {s : [] for s in range(n)}
        visited = set()
        cheapest_price = {}

        for (source, destination, price) in flights:
            graph[source].append([destination, price])

        def travel(source, destination, num_stops):
            if (source, num_stops) in cheapest_price:
                return cheapest_price[(source, num_stops)]
            if source == destination:
                return 0
            if num_stops > k:
                return 1e9

            ans = 1e9
            for (dest, price) in graph[source]:
                ans = min(price + travel(dest, destination, num_stops+1), ans)

            # visited.add(source)
            cheapest_price[(source, num_stops)] = ans
            return ans

        price = travel(src, dst, 0)
        if price >= 1e9:
            return -1
        return price 