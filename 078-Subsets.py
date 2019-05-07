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
        print(path)
        for i in range(index, len(nums)):
            self.dfs(nums, i + 1, results, path + [nums[i]])


if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5]
    result = Solution().subsets(numbers)
    print(result)
    print('Done')
