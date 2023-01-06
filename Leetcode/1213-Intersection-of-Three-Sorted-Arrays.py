from typing import List
import collections


class Solution:
    def arraysIntersection(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
        d = collections.defaultdict(int)
        print(arr1 + arr2 + arr3)
        for num in arr1 + arr2 + arr3:
            d[num] += 1
        return [k for k, v in d.items() if v == 3]


if __name__ == "__main__":
    res = Solution().arraysIntersection(arr1=[1, 2, 3, 4, 5], arr2=[1, 2, 5, 7, 9], arr3=[1, 3, 4, 5, 8])
    print(res)
