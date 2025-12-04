from typing import List

class Solution:
    def maxLength(self, arr: List[str]) -> int:
        def dfs(idx: int, path: str) -> int:
            if len(path) != len(set(path)):
                return 0
            res = len(path)
            for i in range(idx, len(arr)):
                res = max(res, dfs(i + 1, path + arr[i]))
            return res

        return dfs(0, "") 