from typing import List


class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        lens = [i for i in range(1, len(arr) + 1) if i % 2 == 1]
        res = 0
        for l in lens:
            j = 0
            while j + l - 1 < len(arr):
                for i in range(j, j + l):
                    res += arr[i]
                j += 1
        return res


class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        res = 0
        n = len(arr)
        for l in range(1, n + 1, 2):
            for i in range(n - l + 1):
                res += sum(arr[i : i + l])
        return res


if __name__ == "__main__":
    arr = [1, 4, 2, 5, 3]
    res = Solution().sumOddLengthSubarrays(arr)
    print(res)

    arr = [1, 2]
    res = Solution().sumOddLengthSubarrays(arr)
    print(res)

    arr = [10, 11, 12]
    res = Solution().sumOddLengthSubarrays(arr)
    print(res)
