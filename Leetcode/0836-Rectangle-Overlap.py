class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        [x1, y1, x2, y2], [x3, y3, x4, y4] = rec1, rec2
        x, y = (min(x4, x2) - max(x1, x3)), (min(y4, y2) - max(y1, y3))
        return x > 0 and y > 0


class Solution(object):
    def isRectangleOverlap(self, rec1, rec2):
        # check if either rectangle is actually a line
        if (rec1[0] == rec1[2] or rec1[1] == rec1[3] or rec2[0] == rec2[2] or rec2[1] == rec2[3]):
            # the line cannot have positive overlap
            return False

        return not (rec1[2] <= rec2[0] or  # left
                    rec1[3] <= rec2[1] or  # bottom
                    rec1[0] >= rec2[2] or  # right
                    rec1[1] >= rec2[3])  # top

class Solution(object):
    def isRectangleOverlap(self, rec1, rec2):
        def intersect(p_left, p_right, q_left, q_right):
            return min(p_right, q_right) > max(p_left, q_left)
        return (intersect(rec1[0], rec1[2], rec2[0], rec2[2]) and # width > 0
                intersect(rec1[1], rec1[3], rec2[1], rec2[3]))    # height > 0