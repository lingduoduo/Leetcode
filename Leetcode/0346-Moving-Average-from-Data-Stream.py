from collections import deque


class MovingAverage:
    def __init__(self, size: int):
        """Initialize your data structure here."""
        self.size = size
        self.q = deque()
        self.count = 0
        self.sum = 0

    def next(self, val: int) -> float:
        self.count += 1
        self.q.append(val)
        tail = self.q.popleft() if self.count > self.size else 0
        self.sum = self.sum - tail + val
        return self.sum / min(self.size, self.count)


class MovingAverage:
    def __init__(self, size: int):
        self.size = size
        self.queue = []

    def next(self, val: int) -> float:
        size, queue = self.size, self.queue
        queue.append(val)
        # calculate the sum of the moving window
        window_sum = sum(queue[-size:])

        return window_sum / min(len(queue), size)
