from typing import List


class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        res = []
        for i in range(n):
            res.append(nums[i])
            res.append(nums[n + i])
        return res


class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        for i in range(n):
            nums[i] |= nums[i + n] << 10
        ones = int(pow(2, 10)) - 1
        for i in range(n - 1, -1, -1):
            xi = nums[i] & ones
            yi = nums[i] >> 10
            nums[2 * i + 1] = yi
            nums[2 * i] = xi
        return nums
