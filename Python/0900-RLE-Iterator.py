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

if __name__ == "__main__":
    obj = RLEIterator(encoding = [3,8,0,9,2,5])
    res = obj.next(2)
    print(res)
    res = obj.next(1)
    print(res)
    res = obj.next(1)
    print(res)
    res = obj.next(2)
    print(res)