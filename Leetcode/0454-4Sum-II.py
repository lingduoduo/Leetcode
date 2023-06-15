class Solution:
    def fourSumCount(
        self, A: List[int], B: List[int], C: List[int], D: List[int]
    ) -> int:
        d = collections.defaultdict(int)
        for num1 in A:
            for num2 in B:
                d[num1 + num2] += 1

        res = 0
        for num3 in C:
            for num4 in D:
                if -(num3 + num4) in d:
                    res += d[-(num3 + num4)]
        return res
