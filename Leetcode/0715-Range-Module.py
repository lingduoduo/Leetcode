import bisect


class RangeModule:
    def __init__(self):
        self.track = []

    def addRange(self, left: int, right: int) -> None:
        start = bisect.bisect_left(self.track, left)
        end = bisect.bisect_right(self.track, right)

        subtrack = []
        if start % 2 == 0:
            subtrack.append(left)
        if end % 2 == 0:
            subtrack.append(right)

        self.track[start:end] = subtrack

    def queryRange(self, left: int, right: int) -> bool:
        start = bisect.bisect_right(self.track, left)
        end = bisect.bisect_left(self.track, right)

        return start == end and start % 2 == 1

    def removeRange(self, left: int, right: int) -> None:
        start = bisect.bisect_left(self.track, left)
        end = bisect.bisect_right(self.track, right)

        subtrack = []
        if start % 2 == 1:
            subtrack.append(left)
        if end % 2 == 1:
            subtrack.append(right)

        self.track[start:end] = subtrack


# Your RangeModule object will be instantiated and called as such:
# obj = RangeModule()
# obj.addRange(left,right)
# param_2 = obj.queryRange(left,right)
# obj.removeRange(left,right)
import collections
class SegmentTree:
    def __init__(self):
        # store values
        self.tree = collections.defaultdict(int)
        # store lazy values
        self.lazy = collections.defaultdict(int)

    def update(self, query_start, query_end, root_start, root_end, idx, val):
        # no overlap
        if root_end < query_start or query_end < root_start:
            return

        # fully overlap
        if query_start <= root_start and root_end <= query_end:
            self.tree[idx] = val
            self.lazy[idx] = val

        # partially overlap
        else:
            mid = root_start + (root_end - root_start) // 2
            self.push_down(idx)
            self.update(query_start, query_end, root_start, mid, 2 * idx, val)
            self.update(query_start, query_end, mid + 1, root_end, 2 * idx + 1, val)
            self.tree[idx] = self.tree[2 * idx] and self.tree[2 * idx + 1]

    def push_down(self, idx):
        if idx in self.lazy:
            self.tree[2 * idx] = self.lazy[idx]
            self.lazy[2 * idx] = self.lazy[idx]

            self.tree[2 * idx + 1] = self.lazy[idx]
            self.lazy[2 * idx + 1] = self.lazy[idx]

            del self.lazy[idx]

    def query(self, query_start, query_end, root_start, root_end, idx):
        # no overlap
        if root_end < query_start or query_end < root_start:
            return True

        # fully overlap
        if query_start <= root_start and root_end <= query_end:
            return self.tree[idx]

        # partially overlap
        self.push_down(idx)
        mid = root_start + (root_end - root_start) // 2
        return self.query(query_start, query_end, root_start, mid, 2 * idx) and self.query(query_start, query_end, mid + 1, root_end, 2 * idx + 1)

class RangeModule:

    def __init__(self):
        self.tree = SegmentTree()

    def addRange(self, left, right):
        self.tree.update(left, right - 1, 0, 10**9, 1, True)

    def removeRange(self, left, right):
        self.tree.update(left, right - 1, 0, 10**9, 1, False)

    def queryRange(self, left, right):
        return self.tree.query(left, right - 1, 0, 10**9, 1)

# from collections import deque


# class MKAverage:
#     container = None
#     m = None
#     k = None
#     cached = None
#     def __init__(self, m: int, k: int):
#         self.container = deque()
#         self.m = m
#         self.k = k
#         self.cached = None

#     def addElement(self, num: int) -> None:
#         popped = None
#         if len(self.container) < self.m:
#             self.container.append(num)
#         else:
#             popped = self.container.popleft()
#             self.container.append(num)
#         if popped != num:
#             self.cached = None

#     def calculateMKAverage(self) -> int:
#         if len(self.container) < self.m:
#             return -1
#         if self.cached is not None:
#             return self.cached
#         m = self.m
#         k = self.k
#         self.cached = int(sum(sorted(self.container)[k:m-k])/(m-2*k))
#         return self.cached


# Your MKAverage object will be instantiated and called as such:
# obj = MKAverage(m, k)
# obj.addElement(num)
# param_2 = obj.calculateMKAverage()


from collections import deque
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
            if self.smallest[-1]<popped<self.largest[0] and self.smallest[-1]<num<self.largest[0]:
                self.mid_sum+=num-popped
                self.middle.add(num)
                self.middle.remove(popped)

            elif self.smallest[-1]<popped<self.largest[0]:
                self.middle.remove(popped)
                num_small = num<= self.smallest[-1]
                if num_small:
                    self.smallest.add(num)
                    moved = self.smallest.pop()
                else:
                    self.largest.add(num)
                    moved = self.largest.pop(0)
                self.middle.add(moved)
                self.mid_sum += moved-popped
                
            elif popped<= self.smallest[-1]:
                self.smallest.remove(popped)
                self.middle.add(num)
                moved = self.middle.pop(0)
                self.smallest.add(moved)
                self.mid_sum += num-moved
                moved = self.middle.pop()
                self.mid_sum -= moved
                self.largest.add(moved)
                moved = self.largest.pop(0)
                self.mid_sum += moved
                self.middle.add(moved)
                
            elif popped>= self.largest[0]:
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