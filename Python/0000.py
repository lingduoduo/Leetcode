from collections import defaultdict
from typing import List

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: x[0])
        res = [ points[0] ]
        for x, y in points[1:]:
            px, py = res[-1]
            if py < x:
                res.append([x, y])
            else:
                res[-1][1] = min(py, y)
        
        return len(res)

if __name__ == "__main__":
    res = Solution().findMinArrowShots(points = [[10,16],[2,8],[1,6],[7,12]])
    print(res)
