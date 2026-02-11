from typing import List

class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        res = []
        for num in nums:
            if num == 2:
                res.append(-1)
                continue
            
            if (num & 1) == 0:
                res.append(-1)
                continue

            ones = 0
            tmp = num
            while (tmp & 1) == 1:
                ones += 1
                tmp >>= 1
            res.append(num - (1 << (ones - 1)))
        return res


if __name__ == "__main__":
    res = Solution().minBitwiseArray(nums = [2,3,5,7])
    print(res)
