from typing import List


class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        res = 1
        asc, desc = deque([0]), deque([0])
        left, right = 0, 0
        for right in range(1, len(nums)):
            while asc and nums[asc[-1]] > nums[right]:
                asc.pop()
            asc.append(right)

            while desc and nums[desc[-1]] < nums[right]:
                desc.pop()
            desc.append(right)
            while nums[desc[0]] - nums[asc[0]] > limit:
                left += 1
                if desc[0] < left:
                    desc.popleft()
                if asc[0] < left:
                    asc.popleft()
            res = max(res, right - left + 1)
        return res


if __name__ == "__main__":
    nums = [1, 2, 3]
    limit = 4
    result = Solution().longestSubarray(nums, 4)
    print(result)
