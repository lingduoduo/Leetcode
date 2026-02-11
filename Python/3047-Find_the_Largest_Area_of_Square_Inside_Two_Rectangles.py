
from typing import List

class Solution:
    def largestSquareArea(self, bottomLeft: List[List[int]], topRight: List[List[int]]) -> int:
        res = 0
        n = len(bottomLeft)

        for i in range(n):
            for j in range(i + 1, n):
                left = max(bottomLeft[i][0], bottomLeft[j][0])
                right = min(topRight[i][0], topRight[j][0])

                bottom = max(bottomLeft[i][1], bottomLeft[j][1])
                top = min(topRight[i][1], topRight[j][1])

                if left < right and bottom < top:
                    side = min(right - left, top - bottom)
                    res = max(res, side * side)

        return res


if __name__ == "__main__":
    res = Solution().largestSquareArea(bottomLeft = [[1,1],[1,3],[1,5]], topRight = [[5,5],[5,7],[5,9]])
    print(res)