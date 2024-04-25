import collections
from typing import List
from collections import defaultdict

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return None
            
        d = [
            "",  # 0
            "",  # 1
            "abc",  # 2
            "def",  # 3
            "ghi",  # 4
            "jkl",  # 5
            "mno",  # 6
            "pqrs",  # 7
            "tuv",  # 8
            "wxyz"  # 9
        ]

        res = ['']
        for digit in digits: # '2'
            cur = []
            for chr in d[int(digit)]:  #"a", "b", "c"
                for strs in res:
                    cur.append(strs + chr)
            res = cur   


if __name__ == "__main__":
    res = Solution().letterCombinations(digits="23")
    print(res)
            


