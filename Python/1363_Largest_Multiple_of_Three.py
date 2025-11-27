from typing import List

import collections
class Solution:
    def largestMultipleOfThree(self, digits: List[int]) -> str:
        total = sum(digits)
        d = collections.Counter(digits)
        digits.sort(reverse=True)

        def f(i):
            if d[i]:
                digits.remove(i)
                d[i] -= 1
            if not digits: return ''
            if not any(digits): return '0'
            if sum(digits) % 3 == 0: return ''.join(map(str, digits))

        if total % 3 == 0:
            return f(-1)
        if total % 3 == 1 and d[1] + d[4] + d[7]:
            return f(1) or f(4) or f(7)
        if total % 3 == 2 and d[2] + d[5] + d[8]:
            return f(2) or f(5) or f(8)
        if total % 3 == 2:
            return f(1) or f(1) or f(4) or f(4) or f(7) or f(7)
        return f(2) or f(2) or f(5) or f(5) or f(8) or f(8)

if __name__ == "__main__":
    res = Solution().largestMultipleOfThree(digits=[8,1,9])
    print(res)
