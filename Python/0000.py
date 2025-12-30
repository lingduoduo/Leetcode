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
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        tot, cur, start = 0, 0, 0
        n = len(gas)
        for i in range(n):
            print(i, cur, tot)
            tot += gas[(i + 1) % n] - cost[i]
            cur += gas[(i + 1) % n] - cost[i]
            if cur < 0:
                start = i + 1
                cur = 0
        return -1 if tot < 0 else start

if __name__ == "__main__":
    res = Solution().canCompleteCircuit(gas = [5,1,2,3,4], cost = [4,4,1,5,1])
    print(res)

