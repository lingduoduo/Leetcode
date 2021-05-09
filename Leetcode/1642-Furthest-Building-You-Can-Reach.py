class Solution:
    def furthestBuilding(self, heights, bricks: int, ladders: int) -> int:
        n = len(heights)
        q = []
        for idx, num in enumerate(heights):
            if idx == 0:
                continue
            d = heights[idx]-heights[idx-1]
            if d <= 0:
                continue
            heapq.heappush(q, d)
            if len(q) <= ladders:
                continue
            bricks -= heapq.heappop(q)
            if bricks < 0:
                return idx-1
        return n-1

