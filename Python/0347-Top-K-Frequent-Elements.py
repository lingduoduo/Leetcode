import collections
from typing import List


class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        counter = collections.Counter(nums).most_common()
        print(counter)
        return [counter[i][0] for i in range(k)]


class Solution(object):
    def topKFrequent(self, nums, k):
        d = collections.Counter(nums)
        tmp = []
        heapq.heapify(tmp)
        res = []
        for key, val in d.items():
            heapq.heappush(tmp, (-val, key))
        ksmallest = heapq.nsmallest(k, tmp)
        while ksmallest:
            val, key = heapq.heappop(ksmallest)
            res.append(key)
        return res


import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = collections.Counter(nums)
        stack = []
        for i, v in cnt.items():
            heapq.heappush(stack, (v, i))
            if len(stack) > k:
                heapq.heappop(stack)
        res = [i for v, i in stack]
        return res


if __name__ == "__main__":
    nums = [1, 1, 1, 2, 2, 3]
    result = Solution().topKFrequent(nums, 2)
    print(result)
    ###nums = [1]
    ###result = Solution().topKFrequent(nums, 1)
    ###print(result)
