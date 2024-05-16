from typing import List
import collections

class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        d = collections.defaultdict(list)
        for i in range(len(nums)):
            for j in range(len(nums[i])):
                d[i+j].append(nums[i][j])

        res = []
        for k in sorted(d.keys()):
            res.extend(d[k][::-1])
        return res

if __name__ == "__main__":
    res = Solution().findDiagonalOrder(nums=[[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    print(res)
