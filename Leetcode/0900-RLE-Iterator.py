from typing import List

class RLEIterator:

    def __init__(self, encoding: List[int]):
        self.encoding = encoding[::-1]

    def next(self, n: int) -> int:
        acc = 0
        while acc < n:
            if not self.encoding:
                return -1
            times, num = self.encoding.pop(), self.encoding.pop()
            acc += times
        if acc > n:
            self.encoding.append(num)
            self.encoding.append(acc - n)
        return num