import collections
from typing import List


class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        arr = sorted(arr)
        d = collections.Counter(arr)

        res = 0
        keys = list(d.keys())
        for i in range(len(keys)):
            for j in range(i, len(keys)):
                k = target - keys[i] - keys[j]
                if k in keys and k >= keys[j]:
                    if keys[i] < keys[j] < k:
                        res += d[keys[i]] * d[keys[j]] * d[k]
                    elif keys[i] == keys[j] and keys[j] < k:
                        res += d[k] * d[keys[i]] * (d[keys[i]] - 1) // 2
                    elif keys[i] < keys[j] and keys[j] == k:
                        res += d[keys[i]] * d[k] * (d[k] - 1) // 2
                    else:
                        res += d[k] * (d[k] - 1) * (d[k] - 2) // 6

        return res % (10**9 + 7)


if __name__ == "__main__":
    arr = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]
    target = 8
    results = Solution().threeSumMulti(arr, target)
    print(results)
