import collections
class Solution:
    def findLHS(self, nums) -> int:
        res = 0
        d = collections.Counter(nums)

        for k, v in d.items():
            if k-1 in d:
                res = max(res, v+d[k-1])
            if k+1 in d:
                res = max(res, v+d[k+1])
        return res

if __name__ == '__main__':
    # nums = [1,2,3,4]
    # nums = [1,3,2,2,5,2,3,7]
    nums = [1,3,5,7,9,11,13,15,17]
    result = Solution().findLHS(nums)
    print(result)
