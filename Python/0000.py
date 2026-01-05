from typing import List, Optional
from collections import Counter
import heapq
import re
from collections import deque, defaultdict
from typing import List
import random
import bisect
import math


class Solution:
    def countPartitions(self, nums: List[int], k: int) -> int:
        par = []
        for num in nums:
            par.append([num])
        n = len(par)

        res = []
        def dfs(cur, path):
            print(cur, path)
            for i in range(len(path)):
                dfs(cur[-1] + path[i], path[i+1:])
        dfs([[]], par)
        return res

if __name__ == "__main__":
    res = Solution().countPartitions(nums = [9,4,1,3,7], k = 4)
    print(res)
