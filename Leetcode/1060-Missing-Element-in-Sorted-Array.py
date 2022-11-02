class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        # Return how many numbers are missing until nums[idx]
        missing = lambda idx: nums[idx] - nums[0] - idx

        n = len(nums)
        # If kth missing number is larger than
        # the last element of the array
        if k > missing(n - 1):
            return nums[-1] + k - missing(n - 1)

        left, right = 0, n - 1
        # find left = right index such that
        # missing(left - 1) < k <= missing(left)
        while left != right:
            mid = left + (right - left) // 2

            if missing(mid) < k:
                left = mid + 1
            else:
                right = mid

        # kth missing number is greater than nums[left - 1]
        # and less than nums[left]
        return nums[left - 1] + k - missing(left - 1)