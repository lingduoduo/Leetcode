from typing import List
import pysnooper


class Solution:
    @pysnooper.snoop()
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if sum(nums) < target:
            return 0
        left, right = 0, 0
        csum = 0
        res = float("inf")
        while right < len(nums):
            csum += nums[right]
            while target <= csum:
                res = min(res, right - left + 1)
                csum -= nums[left]
                left += 1
            right += 1
        return res

        #


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        presum = [0]
        for num in nums:
            presum.append(presum[-1] + num)

        res = float("inf")
        q = [-1]
        for i in range(len(nums)):
            while q and presum[i + 1] - presum[q[0] + 1] >= target:
                res = min(res, len(q))
                q.pop(0)
            q.append(i)
        return 0 if res == float("inf") else res


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        presum = [0]
        for num in nums:
            presum.append(presum[-1] + num)

        start = 0
        res = float("inf")
        for i, num in enumerate(nums):
            while presum[i + 1] - presum[start] >= target:
                res = min(res, i + 1 - start)
                start += 1
        return 0 if res == float("inf") else res


if __name__ == "__main__":
    # s=15
    # nums = [1,2,3,4,5]
    s = 7
    nums = [2, 3, 1, 2, 4, 3]
    result = Solution().minSubArrayLen(s, nums)
    print(result)
