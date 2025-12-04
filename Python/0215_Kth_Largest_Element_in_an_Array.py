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

def findKthLargest(self, nums: List[int], k: int) -> int:
    heapq.heapify(nums)
    cnt = len(nums)
    while k < cnt:
        heapq.heappop(nums)
        cnt -= 1
    return nums[0]

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
