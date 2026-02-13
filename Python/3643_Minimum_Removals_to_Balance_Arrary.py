
from typing import List
class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        res = n
        r = 0
        for i in range(n):
            while r < n and nums[r] <= nums[i] * k:
                r += 1
            res = min(res, n - (r - i))
        return res


if __name__ == "__main__":
    res = Solution().minRemoval(nums = [1,6,2,9], k = 2)
    print(res)