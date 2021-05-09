class MovingAverage:

    def __init__(self, size: int):
        """ Initialize your data structure here. """
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