import bisect
from itertools import pairwise
from typing import List
from heapq import heappush, heappop, heappushpop

def medianSlidingWindow(self, nums, k):
    if k == 0:
        return []
    res = []
    window = sorted(nums[0:k])

    for i in range(k, len(nums) + 1):
        res.append((window[k // 2] + window[(k - 1) // 2]) / 2.0)
        if i == len(nums):
            break
        index = bisect.bisect_left(window, nums[i - k])
        window.pop(index)
        bisect.insort_left(window, nums[i])
    return res

class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        if k == 1:
            return nums
        if k == 2:
            return [(p + q) / 2 for p,q in pairwise(nums)]
        kodd = k % 2
        ref = sorted(nums[:k])
        hl = [-x for x in ref[:k//2]]
        hl.reverse()
        hr = ref[k//2:]
        if kodd:
            out = [hr[0]]
        else:
            out = [(hr[0] - hl[0]) / 2]
        hrd = []
        hld = []
        def cleanr():
            while hrd and hrd[0] == hr[0]:
                heappop(hrd)
                heappop(hr)

        def cleanl():
            while hld and hld[0] == hl[0]:
                heappop(hld)
                heappop(hl)

        for idx,x in enumerate(nums[k:]):
            y = nums[idx]
            mid = hr[0]
            if y >= mid:
                if x < mid:
                    x = -heappushpop(hl, -x)
                    cleanl()
                heappush(hr, x)
                heappush(hrd, y)
                cleanr()
            else:
                if x >= mid:
                    x = heappushpop(hr, x)
                    cleanr()
                heappush(hl, -x)
                heappush(hld, -y)
                cleanl()
            if kodd:
                out.append(hr[0])
            else:
                out.append((hr[0] - hl[0]) / 2)
        return out
import heapq
from typing import List

class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        # small: max-heap for the smaller half  -> store (-num, index)
        # large: min-heap for the larger half   -> store ( num, index)
        small, large = [], []
        # delayed[idx] = how many times this index should be lazily deleted
        delayed = {}

        small_size = 0  # number of valid elements in small
        large_size = 0  # number of valid elements in large

        def prune(heap):
            """Pop elements from heap while their index is marked as 'delayed'."""
            nonlocal delayed
            while heap and delayed.get(heap[0][1], 0):
                _, idx = heapq.heappop(heap)
                delayed[idx] -= 1
                if delayed[idx] == 0:
                    del delayed[idx]

        def rebalance():
            """Make sure:
               - large_size == small_size      (even k)
               - large_size == small_size + 1  (odd k, extra in large)
            """
            nonlocal small_size, large_size
            # small has too many -> move one to large
            if small_size > large_size:
                num, idx = heapq.heappop(small)
                small_size -= 1
                heapq.heappush(large, (-num, idx))
                large_size += 1
                prune(small)
            # large has more than one extra -> move one to small
            elif large_size > small_size + 1:
                num, idx = heapq.heappop(large)
                large_size -= 1
                heapq.heappush(small, (-num, idx))
                small_size += 1
                prune(large)

        def add(num, idx):
            """Add a new (num, idx) into one of the heaps."""
            nonlocal small_size, large_size
            if not large or num >= large[0][0]:
                heapq.heappush(large, (num, idx))
                large_size += 1
            else:
                heapq.heappush(small, (-num, idx))
                small_size += 1
            rebalance()

        def remove(num, idx):
            """Logically remove (num, idx) from one of the heaps (lazy deletion)."""
            nonlocal small_size, large_size
            delayed[idx] = delayed.get(idx, 0) + 1

            # Decide which heap it belongs to based on current median boundary
            if large and num >= large[0][0]:
                large_size -= 1
                # If it's at the top, physically prune now
                if large and idx == large[0][1]:
                    prune(large)
            else:
                small_size -= 1
                if small and idx == small[0][1]:
                    prune(small)

            rebalance()

        def get_median() -> float:
            """Return current median from the two heaps."""
            if k % 2 == 1:  # odd: extra element in 'large'
                return float(large[0][0])
            else:  # even: average of max(small) and min(large)
                return (large[0][0] - small[0][0]) / 2.0  # small[0][0] is negative

        # 1) Initialize first window
        for i in range(k):
            add(nums[i], i)
        res = [get_median()]

        # 2) Slide the window
        for i in range(k, len(nums)):
            add(nums[i], i)                  # add new element
            remove(nums[i - k], i - k)       # remove element leaving the window
            res.append(get_median())

        return res
