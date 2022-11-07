class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        results = []
        self.dfs(nums, 0, results, [])
        return results

    def dfs(self, nums, index, results, path):
        results.append(path)
        for i in range(index, len(nums)):
            self.dfs(nums, i + 1, results, path + [nums[i]])


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        self.dfs(nums, 0, [])
        return self.res

    def dfs(self, nums, index, path):
        self.res.append(path)
        for i in range(index, len(nums)):
            self.dfs(nums, i + 1, path + [nums[i]])


class Solution:
    def subsets(self, nums):
        self.res = []
        for i in range(1 + len(nums)):
            self.dfs(nums, i, 0, [])
        return self.res

    def dfs(self, nums, n, idx, path):
        if n == len(path):
            self.res.append(path.copy())
            return

        for i in range(idx, len(nums)):
            path.append(nums[i])
            self.dfs(nums, n, i + 1, path)
            path.pop()


class Solution(object):
    def subsets(self, nums):
        n = len(nums)
        return [[nums[i] for i in range(n) if s & 1 << i > 0] for s in range(1 << n)]
        # for s in range(1 << n):
        #    print(bin(s))


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        output = [[]]
        for num in nums:
            output += [curr + [num] for curr in output]
        return output

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        for i in range(1 + len(nums)):
            self.dfs(nums, i, 0, [])
        return self.res

    def dfs(self, nums, n, idx, path):
        if n == len(path):
            self.res.append(path)
            return

        for i in range(idx, len(nums)):
            self.dfs(nums, n, i + 1, path + [nums[i]])


if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5]
    result = Solution().subsets(numbers)
    print(result)
    print('Done')
