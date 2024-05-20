import functools
import heapq
from multiprocessing import heap
from typing import List

class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        n = len(num)
        res = set()
        @functools.lru_cache(maxsize=None)
        def dfs(start, tot, prev, expr):
            if start == n:
                if tot == target:
                    res.add(expr)
                return

            for end in range(start, n):
                cur = int(num[start: end + 1])
                if start == 0:
                    dfs(end + 1, cur, cur, str(cur))
                else:
                    dfs(end + 1, tot + cur, cur, expr + "+" + str(cur))
                    dfs(end + 1, tot - cur, -cur, expr + "-" + str(cur))
                    dfs(end + 1, tot - prev + cur * prev, cur * prev, expr + "*" + str(cur))
        dfs(0, 0, 0, "")
        return res

if __name__ == "__main__":
    res = Solution().findClosestElements(arr = [1,2,3,4,5], k = 4, x = -1)
    print(res)




