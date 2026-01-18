from typing import List
import random

class LargerNumKey(str):
    def __lt__(x, y):
        return x + y > y + x

class Solution:
    def largestNumber(self, nums):
        largest_num = "".join(sorted(map(str, nums), key=LargerNumKey))
        return "0" if largest_num[0] == "0" else largest_num

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        array = list(map(str, nums))
        array.sort(key=lambda x: x*10, reverse=True)
        if array[0] == "0":
            return "0"
        return ''.join(array)

class Solution:
    def largestNumber(self, nums: List[int]) -> str:

        def pivotsort(nums):
            if len(nums) <= 1: 
                return nums

            pivot = random.choice(nums)
            l, m, r = [], [], []

            for num in nums:
                if str(num) + str(pivot) < str(pivot) + str(num):
                    l.append(num)
                elif str(num) + str(pivot) == str(pivot) + str(num):
                    m.append(num)
                else:
                    r.append(num)   # fixed
            return pivotsort(l) + m + pivotsort(r)

        nums = pivotsort(nums)[::-1]
        strs = list(map(str, nums))  

        ans = ''.join(strs)
        return "0" if ans[0] == "0" else ans


if __name__ == "__main__":
    result = Solution().largestNumber(nums=[3, 30, 34, 5, 9])
    print(result)
