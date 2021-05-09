class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        [x1, y1, x2, y2], [x3, y3, x4, y4] = rec1, rec2
        x, y = (min(x4, x2) - max(x1, x3)), (min(y4, y2) - max(y1, y3))
        return x > 0 and y > 0   