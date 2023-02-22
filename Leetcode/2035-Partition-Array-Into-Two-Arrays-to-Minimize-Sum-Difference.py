from typing import List
from itertools import combinations
import bisect

class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        n = len(nums) // 2
        ans = abs(sum(nums[:n]) - sum(nums[n:]))
        total = sum(nums)
        half = total // 2

        for k in range(1, n):
            left = [sum(comb) for comb in combinations(nums[:n], k)]
            right = [sum(comb) for comb in combinations(nums[n:], n - k)]
            right.sort()
            for x in left:
                r = half - x
                p = bisect.bisect_left(right, r)
                if 0 <= p < len(right):
                    left_ans_sum = x + right[p]
                    right_ans_sum = total - left_ans_sum
                    diff = abs(left_ans_sum - right_ans_sum)
                    ans = min(ans, diff)
        return ans

if __name__ == "__main__":
    res = Solution().minimumDifference(nums = [3,9,7,3])
    print(res)