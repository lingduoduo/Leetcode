class SummaryRanges:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.segs = []

    def addNum(self, val):
        l = len(self.segs)
        left, right = 0, l - 1
        while left <= right:
            mid = left + (
                (right - left) >> 1
            )  # bug1: mid = left + ((right - left) >> 1)
            if self.segs[mid][0] <= val:  # bug2: self.segs[mid][0] >= val
                left = mid + 1
            else:
                right = mid - 1
        # merge
        if (
            left - 1 >= 0
            and left < l
            and self.segs[left - 1][1] + 1 == self.segs[left][0] - 1
            and self.segs[left - 1][1] + 1 == val
        ):
            self.segs[left - 1][1] = self.segs[left][1]
            self.segs.pop(left)
        elif left - 1 >= 0 and self.segs[left - 1][1] + 1 == val:  #
            self.segs[left - 1][1] = val
        elif left < l and self.segs[left][0] - 1 == val:  # put the right
            self.segs[left][0] = val
        elif (
            left - 1 >= 0 and self.segs[left - 1][1] + 1 < val
        ) or left == 0:  # must be inserted
            self.segs.insert(left, [val, val])

    def getIntervals(self):
        return self.segs
