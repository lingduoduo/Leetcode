import pysnooper


class MRUQueue:

    def __init__(self, n: int):
        self.nums = [i + 1 for i in range(n)]

    def fetch(self, k: int) -> int:
        self.data.append(self.data.pop(k - 1))
        return self.data[-1]


# Your MRUQueue object will be instantiated and called as such:
n = 8
obj = MRUQueue(n)
print(obj.fetch(3))
print(obj.fetch(5))
