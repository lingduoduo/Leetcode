import collections
from typing import List


class Solution:
    def largestPalindromic(self, num: str) -> str:
        d = collections.Counter(list(num))
        sorted_d = sorted(d.items(), key=lambda x: x[0], reverse=True)
        even = []
        odd = ""
        flag = False
        for k, v in sorted_d:
            if v % 2 == 1:
                if not flag:
                    odd = k
                    flag = True
            v = v //2
            even.append(k*v)
        res = ''.join(even) + odd + ''.join(even[::-1])
        res = res.lstrip('0').rstrip('0')
        return  res or '0'

if __name__ == "__main__":
    res = Solution().largestPalindromic(num = "1000091")
    print(res)

