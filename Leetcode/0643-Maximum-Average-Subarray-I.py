from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        tmp = 0
        res = float("-inf")

        for idx, num in enumerate(nums):
            tmp += num
            if idx >= k:
                tmp -= nums[idx - k]
            if idx >= k - 1:
                res = max(res, tmp)
        res = res / k

        return res


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        cur = result = sum(nums[0:k])
        for i in range(len(nums) - k):
            cur += nums[i + k] - nums[i]
            result = max(cur, result)
        return float(result) / k


if __name__ == "__main__":
    res = Solution().findMaxAverage(nums=[1, 12, -5, -6, 50, 3], k=4)
    print(res)
