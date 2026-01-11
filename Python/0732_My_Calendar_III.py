class MyCalendarThree:
    def __init__(self):
        self.diff = defaultdict(int)

    def book(self, startTime: int, endTime: int) -> int:
        self.diff[startTime] += 1
        self.diff[endTime] -= 1

        cur = 0
        ans = 0
        for t in sorted(self.diff):
            cur += self.diff[t]
            if cur > ans:
                ans = cur
        return ans