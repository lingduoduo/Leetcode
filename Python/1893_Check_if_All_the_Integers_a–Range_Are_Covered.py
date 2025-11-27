from typing import List


class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        res = []
        for lrange in ranges:
            res.extend([i for i in range(lrange[0], lrange[1] + 1)])
        for i in range(left, right + 1):
            if i not in res:
                return False
        return True


if __name__ == "__main__":
    res = Solution().isCovered(ranges=[[1, 2], [3, 4], [5, 6]], left=2, right=5)
    print(res)

    res = Solution().isCovered(ranges=[[1, 10], [10, 20]], left=21, right=21)
    print(res)
