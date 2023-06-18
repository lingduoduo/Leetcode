from typing import List


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points: return 0

        points = sorted(points, key=lambda x: x[1])
        print(points)
        cur = points[0][1]
        res = 1
        for point in points[1:]:
            if cur < point[0]:
                res += 1
                cur = point[1]
        return res


if __name__ == "__main__":
    res = Solution().findMinArrowShots(points=[[10,10],[2,8],[1,6],[7,12]])
    print(res)

    res = Solution().findMinArrowShots(
        points=[[3, 9], [7, 12], [3, 8], [6, 8], [9, 10], [2, 9], [0, 9], [3, 9], [0, 6], [2, 8]])
    print(res)
