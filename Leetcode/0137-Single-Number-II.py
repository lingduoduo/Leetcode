# class Solution:
#     def singleNumber(self, nums) -> int:
#         return (sum(set(nums))*3 - sum(nums))//2

class Solution:
    def singleNumber(self, nums) -> int:
        res = 0
        for i in range(32):
            ct = 0
            for num in nums:
                ct += (num >> i) & 1
            res |= (ct % 3) << i
        return res - 2 ** 32 if res >> 31 & 1 else res


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        seen_once = seen_twice = 0

        for num in nums:
            seen_once = ~seen_twice & (seen_once ^ num)
            seen_twice = ~seen_once & (seen_twice ^ num)

        return seen_once

if __name__ == '__main__':
    nums = [2, 2, 3, 2]
    results = Solution().singleNumber(nums)
    print(results)
