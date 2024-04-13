from typing import List

class Solution:

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
        start = 0
        csum = 0
        res = float("inf")
        for i, v in enumerate(nums):
            csum += v
            while target <= csum:
                res = min(res, i - start + 1)
                csum -= nums[start]
                start += 1
        return res if res != float("inf") else 0


if __name__ == "__main__":
    # s=15
    # nums = [1,2,3,4,5]
    s = 7
    nums = [2, 3, 1, 2, 4, 3]
    result = Solution().minSubArrayLen(s, nums)
    print(result)
