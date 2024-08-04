from typing import List


class Solution:
    def check(self, nums: List[int]) -> bool:
        if len(nums) <= 1:
            return True

        j = 1
        while j < len(nums):
            if nums[0] <= nums[1]:
                if nums[j - 1] <= nums[j]:
                    j += 1
                elif nums[j:] + nums[:j] == sorted(nums):
                    return True
                else:
                    break
            else:
                if nums[j:] + nums[:j] == sorted(nums):
                    return True
                else:
                    break
        if j == len(nums):
            return True
        return False


if __name__ == "__main__":
    nums = [1, 1, 1]
    res = Solution().check(nums)
    print(res)

    nums = [3, 4, 5, 1, 2]
    res = Solution().check(nums)
    print(res)

    nums = [2, 1, 3, 4]
    res = Solution().check(nums)
    print(res)
