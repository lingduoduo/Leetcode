from collections import defaultdict, deque
from typing import List
import math
import heapq

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        d = defaultdict(list)
        for u, v, w in flights:
            d[u].append((w, v))
        
        que = [(0, 0, src)]
        res = {(src, 0): 0}
        while que:
            w, stop, node = heapq.heappop(que)
            if node == dst:
                return w 
            if stop > k + 1:
                continue

            for nei_w, nei in d[node]:
                new_cost = w + nei_w
                new_stops = stop + 1
                if new_cost < res.get((nei, new_stops), float("inf")):
                    res[(nei, new_stops)] = new_cost
                    heapq.heappush(que, (new_cost, stop + 1, nei))
        return -1 

if __name__ == "__main__":
    res = Solution().findCheapestPrice(n = 4, flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]], src = 0, dst = 3, k = 1)
    print(res)
