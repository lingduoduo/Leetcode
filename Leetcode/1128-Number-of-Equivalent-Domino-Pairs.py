from typing import List


class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        # def equalpairs(a, b, c, d):
        #     return (a==c and b==d) or (a==d and b==c)

        # d = {}
        # res = 0
        # for domino in dominoes:
        #     if domino[0]+domino[1] not in d:
        #         d[domino[0]+domino[1]] = [domino]
        #     else:
        #         for i in range(len(d[domino[0]+domino[1]])):
        #             x, y = d[domino[0]+domino[1]][i]
        #             if equalpairs(domino[0], domino[1], x, y):
        #                 res += 1
        #         d[domino[0]+domino[1]].append(domino)
        # return res

        # res = 0
        # for i in range(len(dominoes)-1):
        #     for j in range(i+1, len(dominoes)):
        #         if equalpairs(dominoes[i][0], dominoes[i][1], dominoes[j][0], dominoes[j][1]):
        #             res += 1
        # return res

        m = [0] * 100
        res = 0
        for d in dominoes:
            k1 = d[0] * 10 + d[1]
            k2 = d[1] * 10 + d[0]
            res += m[k1]
            if k1 != k2:
                res += m[k2]
            m[k1] += 1
        return res


if __name__ == "__main__":
    dominoes = [[1, 2], [2, 1], [3, 4], [5, 6], [3, 4]]
    res = Solution().numEquivDominoPairs(dominoes)
    print(res)
