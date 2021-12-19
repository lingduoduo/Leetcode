from typing import List
class Solution:
    def smallestEqual(self, nums: List[int]) -> int:
        for idx, num in enumerate(nums):
            if idx % 10 == num:
                return idx
        return -1

if __name__ == "__main__":
    res = Solution().smallestEqual(nums = [0,1,2])
    print(res)

    res = Solution().smallestEqual(nums = [4,3,2,1])
    print(res)

    res = Solution().smallestEqual(nums = [1,2,3,4,5,6,7,8,9,0])
    print(res)

    res = Solution().smallestEqual(nums = [2,1,3,5,2])
    print(res)

    res = Solution().smallestEqual(nums=[7,8,3,5,2,6,3,1,1,4,5,4,8,7,2,0,9,9,0,5,7,1,6])
    print(res)