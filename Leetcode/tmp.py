from  collections import Counter
from typing import List
import collections
class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        res = ""
        for i, c in enumerate(s):
            if spaces and i == spaces[0]:
                res += " "
                spaces.pop(0)
            res += c
        return res

if __name__ == "__main__":
    res = Solution().addSpaces(s = "LeetcodeHelpsMeLearn", spaces = [8,13,15])
    print(res)

