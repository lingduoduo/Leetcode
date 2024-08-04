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


from typing import List
import heapq


class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        change_point = []
        for start, end, height in buildings:
            # 1 means the start of the building
            # -1 means the end of the building
            change_point.append([start, 1, height])
            change_point.append([end, -1, height])
        change_point.sort(key=lambda x: [x[0], -x[1], -x[2]])
        res = []
        heap = []  # height
        remove_heap = []
        for i, (position, flag, height) in enumerate(change_point):
            # add a building
            if flag == 1:
                heapq.heappush(heap, -height)
            # remove a building
            else:
                heapq.heappush(remove_heap, -height)
            # remove all the removed height, to avoid taking the removed height as the highest
            while len(remove_heap) > 0 and heap[0] == remove_heap[0]:
                heapq.heappop(heap)
                heapq.heappop(remove_heap)
            # no building at the current position
            if len(heap) == 0:
                res.append([position, 0])
            else:
                # take consideration of the first and the last one
                # if the current max height equals the last height(two adjacent buildings), continue
                # if the current position has multiple operations(only take the highest one), continue
                if (
                    i == 0
                    or i == len(change_point) - 1
                    or (-heap[0] != res[-1][1] and position != change_point[i + 1][0])
                ):
                    res.append([position, -heap[0]])  # current max height
        return res
