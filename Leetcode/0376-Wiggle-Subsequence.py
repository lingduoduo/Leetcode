from typing import List


class Solution:
    def wiggleMaxLength(self, nums) -> int:
        n = len(nums)
        if n <= 1:
            return n

        inc, dec = 1, 1
        for x in range(1, n):
            print([inc, dec])
            if nums[x] > nums[x - 1]:
                inc = dec + 1
            elif nums[x] < nums[x - 1]:
                dec = inc + 1
        return max(inc, dec)


class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return n

        res = 1
        last_wiggle = None

        for i in range(1, n):
            diff = nums[i] - nums[i - 1]
            if (diff > 0 and last_wiggle != 1) or (diff < 0 and last_wiggle != -1):
                res += 1
                last_wiggle = 1 if diff > 0 else -1

        return res


if __name__ == "__main__":
    nums = [1, 17, 5, 10, 13, 15, 10, 5, 16, 8]
    res = Solution().wiggleMaxLength(nums)
    print(res)

[x - y for x, y in zip(nums[:-1], nums[1:])]
