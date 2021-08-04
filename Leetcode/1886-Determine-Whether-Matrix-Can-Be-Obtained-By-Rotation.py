from typing import List
class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        rep = 4
        t = 0
        tmp = mat
        while t < rep:
            res = []
            if t == 0:
                tmp = mat

            for col in zip(*tmp):
                res.append([i for i in col[::-1]])

            if res == target:
                return True

            tmp = res
            t += 1

        return False

if __name__ == '__main__':
    res = Solution().findRotation(mat=[[0,1],[1,0]], target=[[1,0],[0,1]])
    print(res)

    res = Solution().findRotation(mat = [[0,1],[1,1]], target = [[1,0],[0,1]])
    print(res)

    res = Solution().findRotation(mat = [[0,0,0],[0,1,0],[1,1,1]], target = [[1,1,1],[0,1,0],[0,0,0]])
    print(res)