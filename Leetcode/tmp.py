import functools
import heapq
from multiprocessing import heap
from typing import List
from itertools import accumulate

class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        nums = [1,2,3,4, 5]
        return list(accumulate(nums))



if __name__ == "__main__":
    res = Solution().addOperators("12345", 5)
    print(res)




