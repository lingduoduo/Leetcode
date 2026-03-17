from typing import List
import heapq
from collections import defaultdict
import random

class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        l = 0
        res = []
        for ch in s:
            if ch == "(":
                l += 1
                res.append(ch)
            elif ch == ")":
                if l > 0:
                    l -= 1
                    res.append(ch)
            else:
                res.append(ch)

        for i in reversed(range(len(res))):
            if res[i] == "(" and l > 0:
                res[i] = ""
                cnt -= 1
        return ''.join(res)

    



if __name__ == "__main__":
    res = Solution().minRemoveToMakeValid(s = "lee(t(c)o)de)")
    print(res)
