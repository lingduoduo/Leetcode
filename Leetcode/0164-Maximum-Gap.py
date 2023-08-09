class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0

        nums.sort()

        res = float("-inf")

        for i in range(1, len(nums)):
            res = max(res, abs(nums[i] - nums[i - 1]))

        return res


class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return 0

        mn, mx = min(nums), max(nums)
        step = max(1, (mx - mn) // (len(nums) - 1))
        size = (mx - mn) // step + 1
        buckets = [[float("inf"), float("-inf")] for _ in range(size)]

        for num in nums:
            i = (num - mn) // step
            bucket_mn, bucket_mx = buckets[i]
            buckets[i] = min(bucket_mn, num), max(bucket_mx, num)

        res = 0
        prev = mn
        for i in range(size):
            bucket_mn, bucket_mx = buckets[i]
            if bucket_mn < float("inf"):
                res = max(res, bucket_mn - prev)
                prev = bucket_mx
        return res
