from typing import List


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0

        points = sorted(points, key=lambda x: x[1])
        cur = points[0][1]
        res = 1
        for point in points[1:]:
            if cur < point[0]:
                res += 1
                cur = point[1]
        return res


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if len(points) == 0:
            return 0
        points.sort(key=lambda x: x[0])
        result = 1
        for i in range(1, len(points)):
            if points[i][0] > points[i - 1][1]:  # 气球i和气球i-1不挨着，注意这里不是>=
                result += 1
            else:
                points[i][1] = min(points[i - 1][1], points[i][1])  # 更新重叠气球最小右边界
        return result


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points = sorted(points, key=lambda x: x[0])
        stack = [points[0]]
        res = 1
        for point in points[1:]:
            if stack[-1][1] < point[0]:
                res += 1
                stack.append(point)
            else:
                stack[-1][1] = min(stack[-1][1], point[1])
        return res


if __name__ == "__main__":
    res = Solution().findMinArrowShots(points=[[10, 10], [2, 8], [1, 6], [7, 12]])
    print(res)

    res = Solution().findMinArrowShots(
        points=[
            [3, 9],
            [7, 12],
            [3, 8],
            [6, 8],
            [9, 10],
            [2, 9],
            [0, 9],
            [3, 9],
            [0, 6],
            [2, 8],
        ]
    )
    print(res)
