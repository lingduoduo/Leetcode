# class Solution:
#     def findSubsequences(self, nums):
        # res = set()
        # n = len(nums)
        # for i in range(1 << n):
        #     epoch = []
        #     for j in range(n):
        #         if (i & 1 << j > 0):
        #             epoch.append(nums[j])
        #     if len(epoch) > 1 and epoch == sorted(epoch):
        #         res.add(tuple(epoch))
        # return list(res)

class Solution:
    def findSubsequences(self, nums):
        dp = set()
        for num in nums:
            for last in list(dp):
                if num >= last[-1]:
                    dp.add(last + (num, ))
            dp.add((num, ))
        return [last for last in dp if len(last) >= 2]

if __name__ == '__main__':
    nums = [4, 6, 7, 7]
    res = Solution().findSubsequences(nums)
    print(res)

    nums = [4,3,2,1]
    res = Solution().findSubsequences(nums)
    print(res)
