
# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end

class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        intervals = []
        for i in schedule:
            [intervals.append(x) for x in i]
        

        intervals.sort(key = lambda x: x.start)
        merged = []
        for i in intervals:
            if not merged or i.start > merged[-1].end:
                merged.append(i)
            else:
                merged[-1].end = max(i.end, merged[-1].end)

        free = []
        for i in range(1, len(merged)):
            free.append(Interval(start=merged[i-1].end, end=merged[i].start))
        return free