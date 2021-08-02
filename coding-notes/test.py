class Solution:
    def reOrderArray(self, nums):
        n = len(nums)
        for i in reversed(range(len(nums))):
            for j in range(i):
                if nums[i] % 2 == 1 and nums[j] % 2 == 0:
                    nums[i], nums[j] = nums[j], nums[i]
        return nums

if __name__ == '__main__':
    res = Solution().reOrderArray(nums=[1, 2, 3, 4, 5])
    print(res)

    res = Solution().reOrderArray(nums=[1, 2, 3, 4, 5, 6])
    print(res)