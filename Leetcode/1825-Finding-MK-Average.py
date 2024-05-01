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
        


from sortedcontainers import SortedList
class MKAverage:

    def __init__(self, m: int, k: int):
        self.smallest = SortedList()
        self.middle = SortedList()
        self.largest = SortedList()
        self.container = deque()
        self.mid_sum = None
        self.m = m
        self.k = k
 
    def addElement(self, num: int) -> None:
        if len(self.container) < self.m:
            self.container.append(num)
            if len(self.container) == self.m:
                sorted_result = sorted(self.container)
                self.smallest = SortedList(sorted_result[:self.k])
                self.middle = SortedList(sorted_result[self.k:self.m-self.k])
                self.largest = SortedList(sorted_result[-self.k:])
                self.mid_sum = sum(self.middle)
        else:
            popped = self.container.popleft()
            self.container.append(num)
            if self.smallest[-1] < popped < self.largest[0] and self.smallest[-1] < num <self.largest[0]:
                self.mid_sum += num - popped
                self.middle.add(num)
                self.middle.remove(popped)

            elif self.smallest[-1] < popped < self.largest[0]:
                self.middle.remove(popped)
                if num <= self.smallest[-1]:
                    self.smallest.add(num)
                    moved = self.smallest.pop()
                else:
                    self.largest.add(num)
                    moved = self.largest.pop(0)
                self.middle.add(moved)
                self.mid_sum += moved - popped
                
            elif popped <= self.smallest[-1]:
                self.smallest.remove(popped)
                self.middle.add(num)
                moved = self.middle.pop(0)
                self.smallest.add(moved)
                self.mid_sum += num - moved
                moved = self.middle.pop()
                self.mid_sum -= moved
                self.largest.add(moved)
                moved = self.largest.pop(0)
                self.mid_sum += moved
                self.middle.add(moved)
                
            elif popped >= self.largest[0]:
                self.largest.remove(popped)
                self.middle.add(num)
                moved = self.middle.pop()
                self.largest.add(moved)
                self.mid_sum += num-moved
                moved = self.middle.pop(0)
                self.mid_sum -= moved
                self.smallest.add(moved)
                moved = self.smallest.pop()
                self.mid_sum += moved
                self.middle.add(moved)

    def calculateMKAverage(self) -> int:
        if len(self.container) < self.m:
            return -1
        return self.mid_sum // (self.m - 2* self.k)


# Your MKAverage object will be instantiated and called as such:
# obj = MKAverage(m, k)
# obj.addElement(num)
# param_2 = obj.calculateMKAverage()

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


        