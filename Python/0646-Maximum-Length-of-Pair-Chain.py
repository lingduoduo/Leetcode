from typing import List


class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        if not pairs:
            return 0

        s = sorted(pairs, key=lambda x: x[1])
        res = 0
        stack = [s[0]]

        for x1, y1 in s:
            x0, y0 = stack[-1]
            if y0 < x1:
                stack.append([x1, y1])

        return len(stack)


if __name__ == "__main__":
    pairs = [[2, 3], [3, 4], [1, 2]]
    res = Solution().findLongestChain(pairs)
