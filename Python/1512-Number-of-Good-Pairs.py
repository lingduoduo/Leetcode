class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        res = 0

        d = collections.defaultdict(list)
        for idx, num in enumerate(nums):
            d[num].append(idx)

        for k, v in d.items():
            if len(v) < 2:
                continue
            else:
                n = len(v)
                res += n * (n - 1) // 2
        return res
