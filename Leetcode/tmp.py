from typing import List

class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        res = 0
        tot = nums[0] + nums[1]
        for num in nums[2:]:
            if tot > num:
                res = tot + num
            tot += num
        return -1 if res == 0 else res

if __name__ == "__main__":
    res = Solution().largestPerimeter(nums = [5, 5, 5])
    print(res)