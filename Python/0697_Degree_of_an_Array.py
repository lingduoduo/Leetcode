class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        d = collections.defaultdict(list)
        degree = 0
        for idx, num in enumerate(nums):
            d[num] += [idx]
            degree = max(degree, len(d[num]))
        res = len(nums)
        for k, v in d.items():
            if len(d[k]) == degree:
                res = min(res, max(d[k]) - min(d[k]) + 1)
        return res


from typing import List
import collections


class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        cnt = collections.Counter(nums)
        max_cnt = max(cnt.values())

        d = collections.defaultdict(list)
        res = float("inf")
        for idx, num in enumerate(nums):
            if cnt[num] == max_cnt:
                if len(d[num]) <= 1:
                    d[num].append(idx)
                else:
                    d[num][-1] = idx
        for k, v in d.items():
            res = min(res, max(v) - min(v) + 1)
        return res


if __name__ == "__main__":
    res = Solution().findShortestSubArray(nums=[1, 2, 2, 3, 1])
    print(res)

    res = Solution().findShortestSubArray(nums=[1, 2, 2, 3, 1, 4, 2])
    print(res)
