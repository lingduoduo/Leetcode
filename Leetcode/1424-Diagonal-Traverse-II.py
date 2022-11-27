from typing import List


class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        res = []
        for i, r in enumerate(nums):
            for j, a in enumerate(r):
                if len(res) <= i + j:
                    res.append([])
                res[i + j].append(a)
        print(res)
        return [x for r in res for x in reversed(r)]


if __name__ == "__main__":
    res = Solution().findDiagonalOrder(nums=[[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    print(res)
