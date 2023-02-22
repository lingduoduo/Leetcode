from itertools import combinations
from bisect import bisect_left
from typing import List

class Solution:
    def minAbsDifference(self, nums: List[int], goal: int) -> int:
        def dfs(i, cur, arr, sums):
            if i == len(arr):
                sums.add(cur)
                return
            dfs(i + 1, cur, arr, sums)
            dfs(i + 1, cur + arr[i], arr, sums)

        sums1, sums2 = set(), set()
        # generate all possible sums of the 1st and 2nd half
        dfs(0, 0, nums[:len(nums) // 2], sums1)
        dfs(0, 0, nums[len(nums) // 2:], sums2)
        print(sums1, sums2)

        # sort the possible sums of the 2nd half
        s2 = sorted(sums2)
        ans = float("inf")
        # for each possible sum of the 1st half, find the sum in the 2nd half
        # that gives a value closest to the goal using binary search
        for s in sums1:
            remain = goal - s
            # binary search for the value in s2 that's closest to the remaining value
            i2 = bisect_left(s2, remain)
            if i2 < len(s2):
                ans = min(ans, abs(remain - s2[i2]))
            if i2 > 0:
                ans = min(ans, abs(remain - s2[i2 - 1]))
        return ans

# class Solution:
#     def minAbsDifference(self, nums: List[int], goal: int) -> int:
#         # generate all possible sums of the 1st and 2nd half
#         n = len(nums) // 2
#         left, right = [0], [0]
#         for k in range(1, n + 1):
#             left.extend([sum(comb) for comb in combinations(nums[:n], k)])
#             right.extend([sum(comb) for comb in combinations(nums[n:], k)])
#
#         # sort the possible sums of the 2nd half
#         s2 = sorted(right)
#         ans = float("inf")
#         # for each possible sum of the 1st half, find the sum in the 2nd half
#         # that gives a value closest to the goal using binary search
#         for s in left:
#             remain = goal - s
#             # binary search for the value in s2 that's closest to the remaining value
#             i2 = bisect_left(right, remain)
#             if i2 < len(right):
#                 ans = min(ans, abs(remain - right[i2]))
#             if i2 > 0:
#                 ans = min(ans, abs(remain - right[i2 - 1]))
#         return ans

if __name__ == "__main__":
    # res = Solution().minAbsDifference(nums = [5,-7,3,5], goal = 6)
    # print(res)

    res = Solution().minAbsDifference(nums = [7,-9,15,-2], goal = -5)
    print(res)

