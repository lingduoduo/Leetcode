class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        events = []
        for l, r, h in buildings:
            events.append([l, -h, r])
            events.append([r, 0, -1])
        events.sort()
        
        res, hp = [], [(0, float("inf"))]
        for l, h, r in events:
            while l >= hp[0][1]: 
                heapq.heappop(hp) 
            if h:
                heapq.heappush(hp, (h, r))
            if not res or res[-1][1] != -hp[0][0]: 
                res.append([l, -hp[0][0]])
        return res
