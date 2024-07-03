from typing import List

class Solution:
    def cal(x):
        ...

    def findClosestNumber(self, nums: List[int]) -> int:
        nums_ = list(map(abs, nums))
        res = [[y, x] for x, y in zip(nums, nums_)]
        res.sort(key=lambda x: (x[0], -x[1]))
        return res[0][1]


if __name__ == "__main__":
    res = Solution().findClosestNumber(nums = [-1000,-1000])
    print(res)