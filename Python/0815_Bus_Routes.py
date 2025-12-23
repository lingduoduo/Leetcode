from typing import List
from collections import deque, defaultdict

class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0

        to_routes = defaultdict(set)
        for i, route in enumerate(routes):
            for stop in route:
                to_routes[stop].add(i)

        q = deque([(source, 0)])  # (current_stop, buses_taken)
        seen_stops = {source}
        used_routes = set()

        while q:
            stop, cnt = q.popleft()
            if stop == target:
                return cnt

            for r in to_routes[stop]:
                if r in used_routes:
                    continue
                used_routes.add(r)

                # boarding route r costs +1 bus
                for nxt_stop in routes[r]:
                    if nxt_stop not in seen_stops:
                        seen_stops.add(nxt_stop)
                        q.append((nxt_stop, cnt + 1))
        return -1

if __name__ == "__main__":
    res = Solution().numBusesToDestination(routes = [[1,2,7],[3,6,7]], source = 1, target = 6)
    print(res)

