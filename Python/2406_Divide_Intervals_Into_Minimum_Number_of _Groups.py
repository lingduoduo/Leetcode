from typing import List
from collections import Counter
import heapq
import re
from collections import defaultdict, deque

class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        que = []
        for x, y in intervals:
            que.append([x, 1])
            que.append([y, -1])
        
        que.sort(key=lambda x: (x[0], -x[1]))
        res = 0
        cnt = 0
        for _, val in que:
            cnt += val
            res = max(res, cnt)
        return res


if __name__ == "__main__":
    res = Solution().minGroups(intervals = [[1,3],[5,6],[8,10],[11,13]])
    print(res)