class Solution:
    """
    input = [2,2,3,4]
    """

    def triangleNumber(self, nums):
        nums = sorted(nums, reverse=True)
        res = 0

        n = len(nums)
        for i in range(n - 2):
            left = i + 1
            right = n - 1
            while left < right:
                if nums[left] + nums[right] > nums[i]:
                    res += right - left
                    left += 1
                else:
                    right -= 1

        return res


if __name__ == "__main__":
    input = [2, 2, 3, 4]
    result = Solution().triangleNumber(input)
    print(result)
