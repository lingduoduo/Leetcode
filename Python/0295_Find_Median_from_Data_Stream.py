from heapq import heappush, heappop, nlargest, nsmallest


class MedianFinder(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        ####heap from small to large
        self.small = []
        self.large = []

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        if not self.small or -num >= self.small[0]:
            heappush(self.small, -num)
        else:
            heappush(self.large, num)

        if len(self.small) < len(self.large):
            n = heappop(self.large)
            heappush(self.small, -n)
        elif len(self.small) - len(self.large) == 2:
            n = heappop(self.small)
            heappush(self.large, -n)

    def findMedian(self):
        """
        :rtype: float
        """
        ###print(self.small)
        ###print(self.large)
        if len(self.small) > len(self.large):
            return -self.small[0]
        else:
            return (-self.small[0] + self.large[0]) / 2


class MedianFinder:
    def __init__(self):
        """
        initialize your data structure here.
        """
        ## heap from small to large
        self.lo = []
        self.hi = []

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        heappush(self.lo, -num)  # lo is maxheap, so -1 * num
        heappush(self.hi, -self.lo[0])  # hi is minheap
        heappop(self.lo)

        if len(self.lo) < len(self.hi):
            heappush(self.lo, -self.hi[0])
            heappop(self.hi)

    def findMedian(self):
        """
        :rtype: float
        """
        if len(self.lo) > len(self.hi):
            return -self.lo[0]
        else:
            return (self.hi[0] - self.lo[0]) / 2  # - as low has -ve values


class MedianFinder:

    def __init__(self):
        self.lo = []  # max heap (store negatives)
        self.hi = []  # min heap

    def addNum(self, num: int) -> None:
        if not self.lo or num <= -self.lo[0]:
            heapq.heappush(self.lo, -num)
        else:
            heapq.heappush(self.hi, num)

        # rebalance heaps
        if len(self.lo) > len(self.hi) + 1:
            heapq.heappush(self.hi, -heapq.heappop(self.lo))
        elif len(self.hi) > len(self.lo):
            heapq.heappush(self.lo, -heapq.heappop(self.hi))

    def findMedian(self) -> float:
        if len(self.lo) == len(self.hi):
            return (-self.lo[0] + self.hi[0]) / 2
        return float(-self.lo[0])
    

if __name__ == "__main__":
    obj = MedianFinder()
    obj.addNum(1)
    obj.addNum(2)
    param_2 = obj.findMedian()
    print(param_2)
    obj.addNum(3)
    param_2 = obj.findMedian()
    print(param_2)
