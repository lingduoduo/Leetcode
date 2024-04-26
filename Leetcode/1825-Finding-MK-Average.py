from collections import deque
from sortedcontainers import SortedList

class MKAverage:

    def __init__(self, m: int, k: int):
        self.queue = deque([])
        self.sorted_list = SortedList()
        self.m = m
        self.k = k
        
    def addElement(self, num: int) -> None:
        if len(self.queue) >= self.m: 
            val = self.queue.popleft()
            self.sorted_list.remove(val)
        self.queue.append(num)
        self.sorted_list.add(num)
        
    def calculateMKAverage(self) -> int:
        if len(self.queue) < self.m: return -1
        print(self.sorted_list)
        return sum(
            self.sorted_list[self.k: len(self.sorted_list) - self.k]
        ) // (self.m - self.k * 2)
        

if __name__ == '__main__':
    obj = MKAverage(m=3, k=1)
    obj.addElement(3)
    obj.addElement(1) 
    res = obj.calculateMKAverage()
    obj.addElement(5)
    obj.addElement(5)
    obj.addElement(5)
    res = obj.calculateMKAverage()
    print(res)


        