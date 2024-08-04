"""
Input: [2, 6, 4, 8, 10, 9, 15]
Output: 5
"""


class Solution:
    def findUnsortedSubarray(self, nums) -> int:
        ###Method 1
        if nums == sorted(nums):
            return 0

        res = len(nums)
        for i in range(len(nums) - 1):
            if nums[i] <= min(nums[i + 1 :]):
                res -= 1
            else:
                break

        if res == 1:
            return 0

        for i in range(len(nums) - 1, 0, -1):
            if nums[i] >= max(nums[:i]):
                res -= 1
            else:
                break
        return res

        ###Method 2
        _len, _nums = len(nums), sorted(nums)
        if nums == _nums:
            return 0
        l = min([i for i in range(_len) if nums[i] != _nums[i]])
        r = max([i for i in range(_len) if nums[i] != _nums[i]])
        return r - l + 1


if __name__ == "__main__":
    ###nums = [2, 6, 4, 8, 10, 9, 15]
    ###result = Solution().findUnsortedSubarray(nums)
    ###print(result)
    #
    ###nums = [1,2,3,4]
    ###result = Solution().findUnsortedSubarray(nums)
    ###print(result)

    nums = [1, 2, 3, 3, 3]
    result = Solution().findUnsortedSubarray(nums)
    print(result)
