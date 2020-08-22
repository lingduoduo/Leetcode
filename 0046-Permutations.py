class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # first try
        #     res = []
        #     self.dfs(nums, res, [])
        #     return res
        
        # def dfs(self, nums, res, path):
        #     if not nums:
        #         res.append(path)
        #     else:
        #         for i in range(len(nums)):
        #             self.dfs(nums[:i] + nums[i + 1:], res, path + [nums[i]])
        
    # second try
    #     res = []
    #     self.tot = len(nums)
    #     self.dfs(nums, res, 0, [])
    #     return res
    #
    # def dfs(self, nums, res, depth, path):
    #     if depth == self.tot:
    #         res.append(path)
    #     else:
    #         for i in range(len(nums)):
    #             self.dfs(nums[:i] + nums[i + 1:], res,
    #                      depth + 1, path + [nums[i]])

    # third try
        if len(nums) <= 1:
            return [nums]
        
        res = []
        for i, num in enumerate(nums):
            n = nums[:i] + nums[i+1:]
            for y in self.permute(n):
                res.append([num]+y)
        return res
        
        

if __name__ == "__main__":
    nums = [1, 2, 3]
    result = Solution().permute(nums)
    print(result)
