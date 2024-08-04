class LargerNumKey(str):
    def __lt__(x, y):
        return x + y > y + x

class Solution:
    def largestNumber(self, nums):
        largest_num = "".join(sorted(map(str, nums), key=LargerNumKey))
        return "0" if largest_num[0] == "0" else largest_num


class Solution:
    def largestNumber(self, nums):
        cur = ""
        res = ""
        nums = [str(num) for num in nums]
        while nums:
            for i in nums:
                if not cur:
                    cur = i
                else:
                    if int(i + cur) > int(cur + i):
                        cur = i
            res += cur
            nums.remove(cur)
            cur = ""
        return str(int(res))

import functools
from typing import List
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        # Custom Comparator
        def custom_sort(a, b):  # a & b are Strings
            if a + b > b + a:
                return 1
            elif a + b < b + a:
                return -1
            else:  # b + a = a + b:
                return 0

        str_nums = list(map(str, nums))
        custom_sorted_nums = sorted(str_nums, key=functools.cmp_to_key(custom_sort), reverse=True)
        return ''.join(custom_sorted_nums).lstrip('0') or "0"


if __name__ == "__main__":
    result = Solution().largestNumber(nums=[3, 30, 34, 5, 9])
    print(result)
