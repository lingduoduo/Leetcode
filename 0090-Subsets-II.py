# class Solution:
#     def subsetsWithDup(self, nums):
#         res = []
#         nums.sort()
#         self.dfs(nums, 0, res, [])
#         return res
        
#     def dfs(self, nums, index, res, path):
#         if path not in res:
#             res.append(path)
#         for i in range(index, len(nums)):
#             self.dfs(nums, i + 1, res, path + [nums[i]])


class Solution:
    def subsetsWithDup(self, nums):
        self.res = []
        nums.sort()
        for i in range(len(nums)):
            self.dfs(nums, i, [])
        return self.res
        
    def dfs(self, nums, index, path):
        if path not in self.res:
            self.res.append(path)
        for i in range(index, len(nums)):
            self.dfs(nums, i + 1, path + [nums[i]])


if __name__ == '__main__':
    Input = [1,2,2]
    result = Solution().subsetsWithDup(Input)
    print(result)