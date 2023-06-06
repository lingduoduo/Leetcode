class Solution(object):
    def productExceptSelf(self, nums):
        left = [nums[0]]
        right = [nums[-1]]
        for i in range(1, len(nums)):
            left.append(left[-1] * nums[i])
            right.append(right[-1] * nums[-i - 1])
        right = right[::-1]
        res = [right[1]]
        for i in range(1, len(nums) - 1):
            res.append(left[i - 1] * right[i + 1])
        res.append(left[-2])
        return res


if __name__ == '__main__':
    nums = [1, 2, 3, 4]
    results = Solution().productExceptSelf(nums)
    print(results)

    nums = [-1, 1, 0, -3, 3]
    results = Solution().productExceptSelf(nums)
    print(results)
