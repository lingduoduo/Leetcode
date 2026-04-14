from collections import defaultdict, deque
from typing import List
import math
import heapq

class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target: return 0

        d = defaultdict(list)
        for bus, route in enumerate(routes):
            for stop in route:
                d[stop].append(bus)

        que = deque([source])
        visited_stops = {source}
        visited_buses = set()
        res = 0
        while que:
            res += 1
            for _ in range(len(que)):
                node = que.popleft()
                for bus in d[node]:
                    if bus in visited_buses:
                        continue
                    visited_buses.add(bus)

                    for nei in routes[bus]:
                        if nei == target:
                            return res
                        
                        if nei not in visited_stops:
                            visited_stops.add(nei)
                            que.append(nei)
        return -1



if __name__ == "__main__":
    res = Solution().numBusesToDestination(routes = [[1,2,7],[3,6,7]], source = 1, target = 6)
    print(res)
