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
            self.dfs(nums, i+1, path+[nums[i]])

class Solution:
    def subsets(self, nums):
        self.res = []
        for i in range(1+len(nums)):
            self.dfs(nums, i, 0, [])
        return self.res

    def dfs(self, nums, n, start, curr):
        if  n==len(curr):
            self.res.append(curr.copy())
            return

        for i in range(start, len(nums)):
            curr.append(nums[i])
            self.dfs(nums, n, i+1, curr)
            curr.pop()




if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5]
    result = Solution().subsets(numbers)
    print(result)
    print('Done')
