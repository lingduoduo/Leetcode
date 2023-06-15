class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        dt1 = collections.Counter("balloon")
        dt2 = collections.Counter(text)

        res = float("inf")
        for k1, v1 in dt1.items():
            if k1 in dt2:
                res = min(res, dt2[k1] // v1)
            else:
                return 0
        return res
