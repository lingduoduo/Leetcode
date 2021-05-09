import heapq
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


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)

if __name__ == '__main__':
    nums = [4, 5, 8, 2]
    output = KthLargest(3, nums)
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