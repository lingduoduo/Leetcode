from typing import List


class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        res = 0
        for idx, num in enumerate(arr):
            if idx > 0 and num > arr[res]:
                res += 1

        return res


class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        l = 0
        r = len(arr) - 1
        while l < r:
            m = l + (r - l) // 2
            if arr[m] < arr[m + 1]:
                l = m + 1
            else:
                r = m
        return l


if __name__ == "__main__":
    arr = [0, 1, 0]
    res = Solution().peakIndexInMountainArray(arr)
    print(res)

    arr = [0, 2, 1, 0]
    res = Solution().peakIndexInMountainArray(arr)
    print(res)

    arr = [24, 69, 100, 99, 79, 78, 67, 36, 26, 19]
    res = Solution().peakIndexInMountainArray(arr)
    print(res)
