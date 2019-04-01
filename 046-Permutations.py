class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        self.dfs(nums, res, [])
        return res

    def dfs(self, nums, res, path):
        if not nums:
            res.append(path)
        else:
            for i in range(len(nums)):
                self.dfs(nums[:i] + nums[i + 1:], res, path + [nums[i]])


if __name__ == "__main__":
    nums = [1, 2, 3]
    result = Solution().permute(nums)
    print(result)
