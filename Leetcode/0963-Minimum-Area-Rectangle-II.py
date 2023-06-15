import numpy as np


class Solution:
    def minAreaFreeRect(self, points) -> float:
        EPS = 1e-7
        points = set(map(tuple, points))

        ans = float("inf")
        for p1, p2, p3 in itertools.permutations(points, 3):
            p4 = p2[0] + p3[0] - p1[0], p2[1] + p3[1] - p1[1]
            if p4 in points:
                v21 = complex(p2[0] - p1[0], p2[1] - p1[1])
                v31 = complex(p3[0] - p1[0], p3[1] - p1[1])
                if abs(v21.real * v31.real + v21.imag * v31.imag) < EPS:
                    area = abs(v21) * abs(v31)
                    if area < ans:
                        ans = area

        return ans if ans < float("inf") else 0
        # res = []
        # for i in range(len(points)):
        #     for j in range(i+1, len(points)):
        #         x1, y1 = points[i]
        #         x2, y2 = points[j]
        #         res.append(np.sqrt((x1-x2)**2+(y1-y2)**2))
        # res = sorted(res)
        # print(res)

        # return res[0]*res[1] if res[0]==res[1]==res[2]==res[3] else 0


if __name__ == "__main__":
    # points = [[1,2],[2,1],[1,0],[0,1]]
    # points = [[0,1],[2,1],[1,1],[1,0],[2,0]]

    # points = [[0,3],[1,2],[3,1],[1,3],[2,1]]
    points = [[3, 1], [1, 1], [0, 1], [2, 1], [3, 3], [3, 2], [0, 2], [2, 3]]
    result = Solution().minAreaFreeRect(points)
    print(result)
