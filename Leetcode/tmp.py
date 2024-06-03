from  collections import Counter
from typing import List
import collections

class Solution:
    def validArrangement(self, pairs: List[List[int]]) -> List[List[int]]:
        edges = collections.defaultdict()

        for x, y in pairs:
            edges[x] = y


if __name__ == "__main__":
    res = Solution().validArrangement(pairs = [[5,1],[4,5],[11,9],[9,4]])
    print(res)



