from typing import List
import collections


class Solution:
    def containsPattern(self, arr: List[int], m: int, k: int) -> bool:
        for i in range(len(arr) - m):
            if i + m * k <= len(arr) and arr[i : i + m] * k == arr[i : i + m * k]:
                return True
        return False


if __name__ == "__main__":
    # arr = [1,2,4,4,4,4]
    # m = 1
    # k = 3
    # res = Solution().containsPattern(arr, m, k)
    # print(res)

    # arr = [1,2,3,1,2]
    # m = 2
    # k = 2
    # res = Solution().containsPattern(arr, m, k)
    # print(res)

    # arr = [3,2,1,3,3,2,1,3,3,1,2,3,3,2,1,3,2,1,1]
    # m = 1
    # k = 2
    # res = Solution().containsPattern(arr, m, k)
    # print(res)

    arr = [2, 1, 2, 2, 2, 2, 2, 2]
    m = 2
    k = 2
    res = Solution().containsPattern(arr, m, k)
    print(res)
