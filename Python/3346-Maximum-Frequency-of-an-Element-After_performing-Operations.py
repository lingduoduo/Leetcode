from typing import List
from collections import Counter

class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        nums.sort()
        n = len(nums)
        if n == 0:
            return 0

        # Pre-count frequencies of each value (used for the initial answer in Case 1)
        value_freq = Counter(nums)
        max_freq = max(value_freq.values())

        # ------------------------------------------------------
        # Case 1: The target value is an element already in nums
        # Any value v in the interval [target - k, target + k]
        # can be converted into target (each with one operation)
        # ------------------------------------------------------
        left = 0
        window_freq = Counter()      # frequency of values currently in the window
        right = 0

        for target in nums:
            # Expand the right boundary: include all nums[right] <= target + k
            while right < n and nums[right] <= target + k:
                window_freq[nums[right]] += 1
                right += 1

            # Shrink the left boundary: remove values < target - k
            while left < n and nums[left] < target - k:
                window_freq[nums[left]] -= 1
                left += 1

            total_in_range = right - left              # number of elements in [target - k, target + k]
            already_target = window_freq[target]       # elements already equal to target

            # We can convert at most numOperations additional elements into target
            best_for_target = min(
                total_in_range,
                already_target + numOperations
            )

            max_freq = max(max_freq, best_for_target)

        # ------------------------------------------------------
        # Case 2: The target value is a "middle value" not in nums
        # If max - min <= 2k within a window, all numbers in the
        # window can be shifted into some middle value v.
        # But converting each element requires one operation,
        # so frequency is limited by numOperations.
        # ------------------------------------------------------
        left = 0
        for right in range(n):
            # Ensure nums[right] - nums[left] <= 2*k
            while nums[right] - nums[left] > 2 * k:
                left += 1

            window_size = right - left + 1
            best_for_middle = min(window_size, numOperations)
            max_freq = max(max_freq, best_for_middle)

        return max_freq
