class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        self.res = []

        nums.sort()

        self.dfs(nums, 0, [])

        return self.res.sort()

    def dfs(self, nums, index, path):
        if path not in self.res:
            self.res.append(path)

        for i in range(index, len(nums)):
            if i>index and nums[i]==nums[i-1]:
                continue
            self.dfs(nums, i+1, path+[nums[i]])



