import collections


class Solution:
    def maxCount(self, m: int, n: int, ops) -> int:
        return min([x for x, y in ops]) * min([y for x, y in ops])


if __name__ == "__main__":
    m = 3
    n = 3
    ops = [[2, 2], [3, 3]]
    # ops = [[2,2],[3,3],[3,3],[3,3],[2,2],[3,3],[3,3],[3,3],[2,2],[3,3],[3,3],[3,3]]
    res = Solution().maxCount(m, n, ops)
    print(res)
