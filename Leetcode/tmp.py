# Definition for a binary tree node.
import collections
from typing import Optional, List

class Solution:
    def findStrobogrammatic(self, n: int) -> List[str]:
        d = {'1':'1','6':'9','8':'8','9':'6'}
        def dfs(n, is_edge):
            if n == 0:
                return ['']
            if n == 1:
                return ['0', '1', '8']
            prev = dfs(n - 2, False)
            res = [cha2 + cha1 + d[cha2] for cha1 in prev for cha2 in d]
            if not is_edge:
                res.extend(['0' + cha +'0' for cha in prev])
            return res
        return dfs(n, True)


if __name__ == '__main__':
    res = Solution().findStrobogrammatic(n=4)
    print(res)


