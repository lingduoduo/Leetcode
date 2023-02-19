class Solution:
    def numSquarefulPerms(self, nums: List[int]) -> int:
        ret = []
        self.dfs(sorted(nums), [], ret)
        return len(ret)

    def dfs(self, nums, path, ret):
        if not nums:
            ret.append(path)
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue  # skip duplicates
            if path and not self.square(path[-1] + nums[i]):
                continue  # backtracking without going further
            self.dfs(nums[:i] + nums[i + 1:], path + [nums[i]], ret)

    def square(self, num):
        from math import sqrt
        return pow(int(sqrt(num)), 2) == num