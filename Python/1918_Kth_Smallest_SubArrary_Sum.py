class Solution:
    def kthSmallestSubarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        lo, hi = min(nums), sum(nums)

        def count_leq(x: int) -> int:
            # number of subarrays with sum <= x
            cnt = 0
            s = 0
            left = 0
            for right in range(n):
                s += nums[right]
                while s > x:
                    s -= nums[left]
                    left += 1
                cnt += (right - left + 1)
            return cnt

        while lo < hi:
            mid = (lo + hi) // 2
            if count_leq(mid) >= k:
                hi = mid
            else:
                lo = mid + 1
        return lo
