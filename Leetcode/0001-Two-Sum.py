from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = dict()
        d[nums[0]] = 0
        for i in range(1, len(nums)):
            if target - nums[i] in d:
                return [i, d[target - nums[i]]]
            else:
                d[nums[i]] = i

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
