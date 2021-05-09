import collections
class Solution:
    def frequencySort(self, nums):
        d = collections.Counter(nums)
        d_sorted = sorted(d.items(), key = lambda x: (x[1], -x[0]))
        res = []
        for k, v in d_sorted:
            res.extend([k]*v)
        return res
            
if __name__ == '__main__':
	nums = [1,1,2,2,2,3]
	res = Solution().frequencySort(nums)
	print(res)