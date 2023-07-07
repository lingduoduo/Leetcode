from typing import List
import collections
import pysnooper
#
#
# class Solution:
#     @pysnooper.snoop()
#     def totalFruit(self, fruits: List[int]) -> int:
#         d = collections.Counter()
#         i = 0
#         res = 0
#         for j, fruit in enumerate(fruits):
#             d[fruit] += 1
#             while len(d.keys()) > 2:
#                 d[fruits[i]] -= 1
#                 if d[fruits[i]] == 0:
#                     del d[fruits[i]]
#                 i += 1
#             res = max(res, j - i + 1)
#         return res
#

class Solution:
    @pysnooper.snoop()
    def totalFruit(self, fruits: List[int]) -> int:
        d = collections.Counter()
        i = 0
        for j, fruit in enumerate(fruits):
            d[fruit] += 1
            if len(d.keys()) > 2:
                d[fruits[i]] -= 1
                if d[fruits[i]] == 0:
                    del d[fruits[i]]
                i += 1
        return j - i + 1

if __name__ == "__main__":
    # res = Solution().totalFruit(fruits = [0,1,2,2])
    # print(res)

    res = Solution().totalFruit(fruits = [1,2,1,2,3])
    print(res)
