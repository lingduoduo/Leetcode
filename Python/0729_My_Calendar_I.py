from bisect import bisect_left

class MyCalendar:

    def __init__(self):
        self.starts = []
        self.ends = []

    def book(self, start: int, end: int) -> bool:
        idx = bisect_left(self.starts, start)

        # check previous interval
        if idx > 0 and self.ends[idx - 1] > start:
            return False

        # check next interval
        if idx < len(self.starts) and self.starts[idx] < end:
            return False

        self.starts.insert(idx, start)
        self.ends.insert(idx, end)
        return True


###Your MyCalendar object will be instantiated and called as such:
###obj = MyCalendar()
###param_1 = obj.book(start,end)
