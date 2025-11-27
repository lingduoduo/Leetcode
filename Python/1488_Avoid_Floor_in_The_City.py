class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        dic = collections.defaultdict(list)
        ret = [-1] * len(rains)
        to_empty = [] # index
        
        for day,lake in enumerate(rains):
            dic[lake].append(day)
        
        for i in range(len(rains)):
            lake = rains[i]
            if lake:
                if dic[lake] and dic[lake][0] < i:
                    return []
                if dic[lake] and len(dic[lake])>1:
                    heapq.heappush(to_empty,dic[lake][1])
            else:
                if to_empty:
                    ret[i] = rains[heapq.heappop(to_empty)]
                    dic[ret[i]].pop(0)
                else:
                    ret[i] = 1
        return ret