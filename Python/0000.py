from typing import List
from collections import defaultdict

from bisect import bisect_left


class MyCalendar:

    def __init__(self):
        self.intervals = []

    def book(self, startTime: int, endTime: int) -> bool:
        starts = [s for s, e in self.intervals]
        idx = bisect_left(starts, startTime)

        if idx > 0 and self.intervals[idx - 1][1] > startTime:
            return False

        if idx < len(self.intervals) and self.intervals[idx][0] < endTime:
            return False

        self.intervals.insert(idx, [startTime, endTime])
        return True


     


if __name__ == "__main__":
    res = Solution().replaceWords(dictionary=["cat", "bat", "rat"], sentence="the cattle was rattled by the battery")
    print(res)
