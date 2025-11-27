class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        mindist = float("inf")
        idx = -1
        for k, v in enumerate(points):
            x1, y1 = v
            if x == x1 or y == y1:
                dist = abs(x - x1) + abs(y - y1)
                if dist < mindist:
                    idx = k
                    mindist = dist
        return idx
