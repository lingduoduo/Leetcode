from typing import List, Optional
import heapq

from collections import OrderedDict

class Solution:
    def customSortString(self, order: str, s: str) -> str:
        d = {chr: idx for idx, chr in enumerate(order)}

        res = []
        for chr in s:
            if chr in d:
                res.append((d[chr], chr))
            else:
                res.append((float('inf'), chr))
        res.sort(key=lambda x: x[0])
        return "".join([x[1] for x in res])

# Test the code        
if __name__ == '__main__':
    res = Solution().customSortString("cba", "abcd")
    print(res)
