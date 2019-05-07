class Solution:
    '''
    Input: n = 4, k = 2
    Output:
    [
      [2,4],
      [3,4],
      [2,3],
      [1,2],
      [1,3],
      [1,4],
    ]
    '''
    
    def combine(self, n, k):
        
        nums = list()
        for i in range(1, n + 1):
            nums.append(i)
        
        self.res = []
        
        self.dfs(nums, k, [])
        return self.res
    
    def dfs(self, nums, k, path):
        if k == 0:
            if path not in self.res:
                self.res.append(path)
            # print(self.res)
            # print(nums)
            return
        
        while len(nums) >= k:
            self.dfs(nums[1:], k - 1, path + [nums[0]])
            nums.pop(0)


if __name__ == '__main__':
    n = 5
    k = 3
    result = Solution().combine(n, k)
    print(result)
