from typing import List

class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        res = n
        r = 0
        for i in range(n):
            while r < n and nums[i] * k >= nums[r]:
                r += 1
            res = min(res, n - (r - i))
        return res


if __name__ == "__main__":
    res = Solution().minRemoval(nums = [2,1,5], k = 2)
    print(res)

