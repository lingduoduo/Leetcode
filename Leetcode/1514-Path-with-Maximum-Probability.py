class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        maps = defaultdict(list)
        for i in range(len(edges)):
            maps[edges[i][0]].append((edges[i][1], succProb[i]))
            maps[edges[i][1]].append((edges[i][0], succProb[i]))
            
        stack = [(-1, start)]
        
        d = defaultdict(float)
        d[start] = -1
        
        while stack:
            curdist, cur = heapq.heappop(stack)
            if cur == end:
                return -curdist
            for node, prob in maps[cur]:
                tmp = curdist * prob
                if tmp < d[node]:
                    d[node] = tmp
                    heapq.heappush(stack, (tmp, node))
        return 0
