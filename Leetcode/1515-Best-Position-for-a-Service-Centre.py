from typing import List
import numpy as np


class Solution:
    def getMinDistSum(self, positions: List[List[int]]) -> float:
        def dist(a, b):
            res = 0.0
            for x, y in positions:
                res += math.sqrt((x - a) ** 2 + (y - b) ** 2)
            return res

        step = 1.0
        nums = np.array(positions)
        curx, cury = nums.mean(axis=0)
        curdist = dist(curx, cury)

        while step > 0.000001:
            f = True
            for dirx, diry in [(0, step), (0, -step), (step, 0), (-step, 0)]:
                tx, ty = curx + dirx, cury + diry
                tmp = dist(tx, ty)
                if tmp < curdist:
                    curdist = tmp
                    curx, cury = tx, ty
                    f = False
            if f:
                step /= 10
        return curdist
