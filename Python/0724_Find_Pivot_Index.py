from typing import List

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        pre = [0] * len(nums)
        pos = [0] * len(nums)
        n = len(nums)
        for i in range(1, len(nums)):
            pre[i] = pre[i - 1] + nums[i - 1]
            pos[n - i - 1] = pos[n - i] + nums[n - i]

        for i in range(len(nums)):
            if pre[i] == pos[i]:
                return i
        return -1
    
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        tot = sum(nums)
        leftsum = 0
        for i, x in enumerate(nums):
            if leftsum == (tot - leftsum - x):
                return i
            leftsum += x
        return -1

if __name__ == "__main__":
    nums = [1, 7, 3, 6, 5, 6]
    res = Solution().pivotIndex(nums)
    print(res)
