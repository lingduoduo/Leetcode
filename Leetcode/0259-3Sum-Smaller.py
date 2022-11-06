from typing import List

class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        nums.sort()
        res = 0
        for i in range(len(nums)):
            left = i + 1
            right = len(nums) - 1
            while left < right:
                if nums[i] + nums[left] + nums[right] >= target:
                    right -= 1
                else:
                    res += right - left
                    left += 1
        return res


if __name__ == "__main__":
    res = Solution().threeSumSmaller(nums=[-2, 0, 1, 3], target=2)
    print(res)
