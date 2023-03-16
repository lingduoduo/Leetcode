import heapq

class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        ready = [r for r in range(n)]
        rooms = []
        heapq.heapify(ready)
        res = [0] * n
        for s,e in sorted(meetings):
            while rooms and rooms[0][0] <= s:
                t,r = heapq.heappop(rooms)
                heapq.heappush(ready, r)
            if ready:
                r = heapq.heappop(ready)
                heapq.heappush(rooms, [e, r])
            else:
                t,r = heapq.heappop(rooms)
                heapq.heappush(rooms, [t + e - s, r])
            res[r] += 1
        return res.index(max(res))