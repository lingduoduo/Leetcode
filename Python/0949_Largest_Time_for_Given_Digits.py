class Solution:
    def largestTimeFromDigits(self, arr: List[int]) -> str:
        res = -1
        for h1, h2, m1, m2 in itertools.permutations(arr):
            hour = h1 * 10 + h2
            minute = m1 * 10 + m2
            if hour < 24 and minute < 60:
                time = hour * 60 + minute
                res = max(res, time)
        return "%02d:%02d" % divmod(res, 60) if res >= 0 else ""
