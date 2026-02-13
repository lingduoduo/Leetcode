import heapq
from typing import List
import random


class Solution(object):
    def findKthLargest(self, nums, k):
        tmp = sorted(nums)
        return tmp[-k]


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return heapq.nlargest(k, nums)[-1]

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for num in nums:
            heapq.heappush(heap, num)
            if len(heap) > k:
                heapq.heappop(heap)
        return heap[0]

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def quick_select(nums, k):
            pivot = random.choice(nums)
            left, mid, right = [], [], []

            for num in nums:
                if num > pivot:
                    left.append(num)
                elif num < pivot:
                    right.append(num)
                else:
                    mid.append(num)
            if k <= len(left):
                return quick_select(left, k)
            if len(left) + len(mid) < k:
                return quick_select(right, k - len(left) - len(mid))
            return pivot

        return quick_select(nums, k)

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        min_value = min(nums)
        max_value = max(nums)
        freq = [0] * (max_value - min_value + 1)

        for num in nums:
            freq[num - min_value] += 1
        
        remain = k
        for num in range(len(freq) -1, -1, -1):
            remain -= freq[num]
            if remain <= 0:
                return num + min_value

        return -1