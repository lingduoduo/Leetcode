class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        import collections
        d=collections.Counter(nums)
        l=sorted(d.values())[-k:]

        res = list()
        for k, v in d.items():
        	if v in l:
        		res.append(k)
        return res


if __name__=="__main__":
    # nums=[1,1,1,2,2,3]
    # result = Solution().topKFrequent(nums, 2)
    # print(result)
    nums=[1]
    result = Solution().topKFrequent(nums, 1)
    print(result)

