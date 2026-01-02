class Solution(object):
    def nextPermutation(self, nums):
        flag = -1
        for i in reversed(range(len(nums))):
            if nums[i] < nums[i + 1]:
                flag = i
                break

        if flag == -1:
            nums.sort()
        else:
            for i in range(len(nums) - 1, flag, -1):
                if nums[i] > nums[flag]:
                    nums[i], nums[flag] = nums[flag], nums[i]
                    nums[flag + 1 :] = sorted(nums[flag + 1 :])
                    break
        return nums


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        n = len(nums)

        first = -1
        for i in range(n - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                first = i
                break

        if first == -1:
            nums.reverse()
            return

        second = -1
        for i in range(n - 1, first, -1):
            if nums[i] > nums[first]:
                second = i
                break

        # swap pivot and successor
        nums[first], nums[second] = nums[second], nums[first]

        # reverse suffix (in-place slice assignment)
        nums[first + 1:] = nums[first + 1:][::-1]

if __name__ == "__main__":
    nums = [1, 4, 3, 2]
    # nums = [1, 2, 3]
    # nums = [1, 7, 3, 4, 1]
    # nums = [1, 5, 1]
    # nums = [1, 1]
    # nums = [2, 2, 7, 5, 4, 3, 2, 2, 1]
    result = Solution().nextPermutation(nums)
    print(result)
