from typing import List

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for k, v in enumerate(nums):
            i = k + 1
            while i < len(nums):
                if v + nums[i] == target:
                    return ([k, i])
                else:
                    i = i + 1


class Solution(object):
    def twoSum(self, nums, target):
        d = {}
        for i, v in enumerate(nums):
            d[v] = i

        for i in range(len(nums)):
            if (target - nums[i] in d) and d[target - nums[i]] != i:
                return i, d[target - nums[i]]
        return None


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pos = dict()
        for i, num in enumerate(nums):
            if target - num in pos:
                return [pos[target - num], i]
            else:
                pos[num] = i
        return [0, 0]

if __name__ == "__main__":
    numbers = [2, 7, 11, 15]
    result = Solution().twoSum(nums=numbers, target=9)
    print(result)
    numbers = [3, 2, 4]
    result = Solution().twoSum(numbers, 6)
    print(result)
    numbers = [2, 5, 5, 11]
    result = Solution().twoSum(numbers, 6)
    print(result)
    nums = [3, 3]
    target = 6
    result = Solution().twoSum(nums, target)
    print(result)
