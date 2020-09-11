class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums = sorted(nums)
        self.res = []
        self.d = len(nums)
        self.dfs(nums, 0, 0, [])
        return self.res
    
    def dfs(self, nums, idx, depth, path):
        ###print([nums, idx, depth, path])
        if depth == self.d:
            self.res.append(path)
            return
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            self.dfs(nums[:i] + nums[i + 1:], i, depth + 1, path + [nums[i]])


if __name__ == "__main__":
    nums = [1, 1, 3]
    result = Solution().permuteUnique(nums)
    print(result)
