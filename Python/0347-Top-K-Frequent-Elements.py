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
        # 要统计元素出现频率
        map_ = {}  # nums[i]:对应出现的次数
        for i in range(len(nums)):
            map_[nums[i]] = map_.get(nums[i], 0) + 1

        # 对频率排序
        # 定义一个小顶堆，大小为k
        pri_que = []  # 小顶堆

        # 用固定大小为k的小顶堆，扫描所有频率的数值
        for key, freq in map_.items():
            heapq.heappush(pri_que, (freq, key))
            if len(pri_que) > k:  # 如果堆的大小大于了K，则队列弹出，保证堆的大小一直为k
                heapq.heappop(pri_que)

        # 找出前K个高频元素，因为小顶堆先弹出的是最小的，所以倒序来输出到数组
        result = [0] * k
        for i in range(k - 1, -1, -1):
            result[i] = heapq.heappop(pri_que)[1]
        return result


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = collections.Counter(nums)
        stack = []
        for i, v in cnt.items():
            heapq.heappush(stack, (v, i))
            if len(stack) > k:
                heapq.heappop(stack)
        print(stack)
        res = [i for v, i in stack]
        return res


if __name__ == "__main__":
    nums = [1, 1, 1, 2, 2, 3]
    result = Solution().topKFrequent(nums, 2)
    print(result)
    ###nums = [1]
    ###result = Solution().topKFrequent(nums, 1)
    ###print(result)
