import collections


class Solution(object):
    def majorityElement(self, nums):
        d = collections.Counter(nums)
        f = d.most_common()
        return f[0][0]


class Solution(object):
    def majorityElement(self, nums):
        d = collections.Counter(nums)
        return sorted(d.keys(), key=d.get)[-1]


if __name__ == '__main__':
    nums = [2, 2, 1, 1, 1, 2, 2]
    res = Solution().majorityElement(nums)
    print(res)
