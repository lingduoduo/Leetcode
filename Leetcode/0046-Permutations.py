from itertools import permutations
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        return list(permutations(nums))

class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        visited = [0] * len(nums)
        res = []
        
        def dfs(path):
            if len(path) == len(nums):
                res.append(path)
            else:
                for i in range(len(nums)):
                    if not visited[i]:
                        visited[i] = 1
                        dfs(path + [nums[i]])
                        visited[i] = 0
        
        dfs([])
        return res

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
