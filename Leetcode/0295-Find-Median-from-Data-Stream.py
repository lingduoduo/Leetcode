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


if __name__ == "__main__":
    obj = MedianFinder()
    obj.addNum(1)
    obj.addNum(2)
    param_2 = obj.findMedian()
    print(param_2)
    obj.addNum(3)
    param_2 = obj.findMedian()
    print(param_2)
