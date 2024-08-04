import collections


class Solution:
    def smallerNumbersThanCurrent(self, nums):
        res = []
        for i in range(len(nums)):
            res.append(([nums[i] < nums[j] for j in range(len(nums))]).count(True))

        return res


if __name__ == "__main__":
    nums = [8, 1, 2, 2, 3]
    results = Solution().smallerNumbersThanCurrent(nums)
    print(results)
