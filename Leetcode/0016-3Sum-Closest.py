from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        res = float("inf")
        for i in range(n - 2):
            j = i + 1
            k = n - 1
            while j < k:
                val = nums[i] + nums[j] + nums[k]
                if val == target:
                    return val
                elif abs(val - target) < abs(res - target):
                    res = val
                if val < target:
                    j += 1
                else:
                    k -= 1
        return res


if __name__ == "__main__":
    nums = [0, 1, 2]
    # nums = [-1,-5,-3,-4,2,-2]
    # nums = [0, 2, 1, -3]
    result = Solution().threeSumClosest(nums, 3)
    print(result)
