class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        import collections

        ###d = collections.Counter(nums)
        ###l = sorted(d.values())[-k:]

        ###res = list()
        ###for k, v in d.items():
        ###    if v in l:
        ###        res.append(k)
        ###return res

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


if __name__ == "__main__":
    nums = [1, 1, 1, 2, 2, 3]
    result = Solution().topKFrequent(nums, 2)
    print(result)
    ###nums = [1]
    ###result = Solution().topKFrequent(nums, 1)
    ###print(result)
