import heapq
from multiprocessing import heap
from typing import List
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l = 0
        r = len(arr) - k
        while l < r:
            mid= l + (r - l) // 2
            if x <= arr[mid]:
                r = mid
            elif arr[mid + k] <= x:
                l = mid + 1
            else:
                mid_l = abs(x - arr[mid])
                mid_r = abs(x - arr[mid + k])
                if mid_l <= mid_r:
                    r = mid
                else:
                    l = mid + 1
        return arr[l:l + k]


if __name__ == "__main__":
    res = Solution().findClosestElements(arr = [1,2,3,4,5], k = 4, x = -1)
    print(res)




