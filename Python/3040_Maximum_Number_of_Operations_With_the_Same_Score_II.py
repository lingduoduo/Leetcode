from typing import List

class Solution:
    def maxOperations(self, nums: List[int]) -> int:
        def findMaxOpsHelper(left: int, right: int, previousSum: int, memoization: List[List[int]]) -> int:
            if left >= right:
                return 0
            if memoization[left][right] != 0:
                return memoization[left][right]

            res = 0
            if nums[left] + nums[left + 1] == previousSum:
                res = max(res, findMaxOpsHelper(left + 2, right, previousSum, memoization) + 1)
            if nums[left] + nums[right] == previousSum:
                res = max(res, findMaxOpsHelper(left + 1, right - 1, previousSum, memoization) + 1)
            if nums[right] + nums[right - 1] == previousSum:
                res = max(res, findMaxOpsHelper(left, right - 2, previousSum, memoization) + 1)

            memoization[left][right] = res
            return res

        res = 0
        n = len(nums)
        memoization = [[0] * n for _ in range(n)]
        start = 0
        end = n - 1

        res = max(res, findMaxOpsHelper(start + 2, end, nums[start] + nums[start + 1], memoization) + 1)
        res = max(res, findMaxOpsHelper(start + 1, end - 1, nums[start] + nums[end], memoization) + 1)
        res = max(res, findMaxOpsHelper(start, end - 2, nums[end] + nums[end - 1], memoization) + 1)

        return res

