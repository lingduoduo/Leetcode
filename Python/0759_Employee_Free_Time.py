
# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end

class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        intervals = []
        for interval in schedule:
            intervals.extend(interval)
        
        intervals.sort(key=lambda x: x[0])
        merged = [intervals[0]]
        for x, y in intervals:
            px, py = merged[-1]
            if py < x:
                merged.append([x, y])
            else:
                merged[-1][1] = max(py, y)
        
        res = []
        for i in range(1, len(merged)):
            res.append([merged[i-1][1], merged[i][0]])
        return res
