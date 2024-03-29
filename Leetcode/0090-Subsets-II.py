from typing import List


class Solution:
    def subsetsWithDup(self, nums):
        res = []
        nums.sort()
        self.dfs(nums, 0, res, [])
        return res

    def dfs(self, nums, index, res, path):
        if path not in res:
            res.append(path)
        for i in range(index, len(nums)):
            self.dfs(nums, i + 1, res, path + [nums[i]])


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = [[], [nums[0]]]
        cur = [[nums[0]]]
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                cur = [t + [nums[i]] for t in cur]
            else:
                cur = [t + [nums[i]] for t in res]
            res += cur
        return res


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(idx, path):
            nonlocal res
            if sorted(path) not in res:
                res.append(sorted(path))
            for i in range(idx, len(nums)):
                dfs(i + 1, path + [nums[i]])

        dfs(0, [])
        return res


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(idx, path):
            nonlocal res
            res.append(path)
            for i in range(idx, len(nums)):
                if i >= idx + 1 and nums[i - 1] == nums[i]:
                    continue
                dfs(i + 1, path + [nums[i]])

        nums.sort()
        dfs(0, [])
        return list(res)


if __name__ == "__main__":
    Input = [1, 2, 2]
    result = Solution().subsetsWithDup(Input)
    print(result)
