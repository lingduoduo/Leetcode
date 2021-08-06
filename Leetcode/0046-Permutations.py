from itertools import permutations
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        return list(permutations(nums))

class Solution:
    def permute(self, nums):
        self.nums = nums
        self.res = []
        self.visited = [False] * len(self.nums)
        self.dfs([])
        return self.res
    
    def dfs(self, path):
        if len(self.nums) == len(path):
            self.res.append(path[:])
            
        for i in range(len(self.nums)):
            if self.visited[i]:
                continue
            path.append(self.nums[i])
            self.visited[i] = True
            self.dfs(path)
            path.pop()
            self.visited[i] = False

class Solution(object):
    def permute(self, nums):
        self.res = []
        self.dfs(nums, [])
        return self.res

    def dfs(self, curr, path):
        if curr == []:
            self.res.append(path)

        for i in range(len(curr)):
            self.dfs(curr[:i]+curr[i+1:], path+[curr[i]])

if __name__ == "__main__":
    nums = [1, 2, 3]
    result = Solution().permute(nums)
    print(result)
