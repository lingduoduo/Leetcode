from typing import List


class Solution:
    def canChoose(self, groups: List[List[int]], nums: List[int]) -> bool:
        pass


if __name__ == "__main__":
    groups = [[1, -1, -1], [3, -2, 0]]
    nums = [1, -1, 0, 1, -1, -1, 3, -2, 0]
    res = Solution().canChoose(groups, nums)
    print(res)
