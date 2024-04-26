from typing import List
from collections import defaultdict, deque

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: x[0])
        res = 0
        stack = [points[0]]
        for point in points:
            if stack[-1][1] < point[0]:
                res += 1
                stack.append(point)
            else:
                stack[-1][0] = max(stack[-1][0], point[0])
                stack[-1][1] = min(stack[-1][1], point[1])
        return res + 1






if __name__ == "__main__":
   res = Solution().findMinArrowShots([[10,16],[2,8],[1,6],[7,12]])
   print(res)