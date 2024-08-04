import heapq
from typing import List


class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.sorted_num = sorted(nums)
        self.size = len(self.sorted_num)
        self.k = k
        if self.size > self.k:
            self.sorted_num = self.sorted_num[-k:]
        heapq.heapify(self.sorted_num)

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        if self.size < self.k:
            heapq.heappush(self.sorted_num, val)
            self.size += 1
        elif val > self.sorted_num[0]:
            heapq.heappop(self.sorted_num)
            heapq.heappush(self.sorted_num, val)
        return self.sorted_num[0]


from typing import List


class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.stack = []
        for num in nums:
            heapq.heappush(self.stack, -num)
        self.k = k

    def add(self, val: int) -> int:
        heapq.heappush(self.stack, -val)
        print(self.stack)
        val = -heapq.nsmallest(self.k, self.stack)[-1]
        print(val)

        self.sorted_num = sorted(nums)
        self.size = len(self.sorted_num)
        self.k = k
        if self.size > self.k:
            self.sorted_num = self.sorted_num[-k:]


class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.stack = nums
        self.size = len(self.stack)
        self.k = k
        heapq.heapify(self.stack)
        while self.size > k:
            heapq.heappop(self.stack)
            self.size -= 1

    def add(self, val: int) -> int:
        if self.size < self.k:
            heapq.heappush(self.stack, val)
            self.size += 1
        elif val > self.stack[0]:
            heapq.heappop(self.stack)
            heapq.heappush(self.stack, val)
        return self.stack[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)

if __name__ == "__main__":
    nums = [4, 5, 8, 2]
    output = KthLargest(3, nums)
    print(output.add(3))
# # Your KthLargest object will be instantiated and called as such:
# # obj = KthLargest(k, nums)
# # param_1 = obj.add(val)
# Input
# ["KthLargest", "add", "add", "add", "add", "add"]
# [[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]]
# Output
# [null, 4, 5, 5, 8, 8]

# Explanation
# KthLargest kthLargest = new KthLargest(3, [4, 5, 8, 2]);
# kthLargest.add(3);   // return 4
# kthLargest.add(5);   // return 5
# kthLargest.add(10);  // return 5
# kthLargest.add(9);   // return 8
# kthLargest.add(4);   // return 8
