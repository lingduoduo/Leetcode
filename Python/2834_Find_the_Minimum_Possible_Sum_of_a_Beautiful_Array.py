class Solution:
    def minimumPossibleSum(self, n: int, target: int) -> int:
        cnt = 0
        d = set()
        res = []
        while len(res) < n:
            cnt += 1
            if target - cnt not in d:
                d.add(cnt)
                res.append(cnt)
        return sum(res)
