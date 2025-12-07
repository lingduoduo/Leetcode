from typing import List
from collections import Counter
import heapq
import re
from collections import defaultdict, deque

class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        res = 0
        def dfs(idx, path):
            print(path)
            nonlocal res
            if len(path) == k: 
                res = max(res, sum(path))
                return
            
            dfs(idx + 1, path + [cardPoints[idx]])
            dfs(idx + 1, path + [cardPoints[-idx-1]])

        dfs(0, [])
        return res


if __name__ == "__main__":
    res = Solution().maxScore(cardPoints = [1,79,80,1,1,1,200,1], k = 3)
    print(res)