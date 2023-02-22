from itertools import combinations
from bisect import bisect_left
from typing import List


class Solution:
    def minAbsDifference(self, nums: List[int], goal: int) -> int:
        def fn(nums):
            ans = {0}
            for x in nums:
                ans |= {x + y for y in ans}
            return ans

        nums0 = sorted(fn(nums[:len(nums) // 2]))

        ans = inf
        for x in fn(nums[len(nums) // 2:]):
            k = bisect_left(nums0, goal - x)
            if k < len(nums0): ans = min(ans, nums0[k] + x - goal)
            if 0 < k: ans = min(ans, goal - x - nums0[k - 1])
        return ans


if __name__ == "__main__":
    # res = Solution().minAbsDifference(nums = [5,-7,3,5], goal = 6)
    # print(res)

    res = Solution().minAbsDifference(nums=[7, -9, 15, -2], goal=-5)
    print(res)
