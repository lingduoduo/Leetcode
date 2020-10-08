import heapq
from collections import defaultdict
class DinnerPlates:
 
    def __init__(self, capacity: int):
        self.cap = capacity
        self.pq = []
        self.sta = []
        
    def push(self, val: int) -> None:
        def push_at(index, val):
            if (index < 0 or index >= len(self.sta) or len(self.sta[index]) == self.cap):
                self.sta.append([val])
            else:
                self.sta[index].append(val)
        
        insert_idx = heapq.heappop(self.pq) if self.pq else len(self.sta)-1
        push_at(insert_idx, val)
 
    def pop(self) -> int:
        while (self.sta and (not self.sta[-1])):
            self.sta.pop()
            
        return self.popAtStack(len(self.sta)-1)
    
    def popAtStack(self, index: int) -> int:
        if (0 <= index < len(self.sta) and self.sta[index]):
            heapq.heappush(self.pq,index)
            return self.sta[index].pop()
        return -1
