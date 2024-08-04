from typing import List


class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        seen = set()  # track visited elements in the window
        res = tot = 0
        start = 0
        for i in range(len(nums)):
            x = nums[i]
            # adjust the left bound of sliding window until you get all unique elements
            while start < i and x in seen:
                seen.remove(nums[start])
                tot -= nums[start]
                start += 1
            tot += x
            seen.add(x)
            res = max(res, tot)
        return res


class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        res = 0
        q = deque()
        seen = set()  # Using a set for O(1) lookups
        current_sum = 0

        for num in nums:
            while num in seen:
                left_num = q.popleft()
                current_sum -= left_num
                seen.remove(left_num)
            q.append(num)
            seen.add(num)
            current_sum += num
            res = max(res, current_sum)

        return res
