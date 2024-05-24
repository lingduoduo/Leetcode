# Definition for a binary tree node.
import collections
from typing import Optional, List

class Solution:
    def generatePalindromes(self, s: str) -> List[str]:
        cnt = collections.Counter(s)
        print(cnt)



if __name__ == '__main__':
    res = Solution().generatePalindromes(s = "aabb")
    print(res)
