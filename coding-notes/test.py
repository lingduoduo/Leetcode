class Solution:
    def permutation(self, strs: str):
        self.nums = list(strs)
        self.res = []
        self.visited = [False] * len(self.nums)
        self.dfs([])
        return self.res
    
    def dfs(self, path):
        print(path)
        if len(self.nums) == len(path):
            self.res.append(''.join(path[:]))
            
        for i in range(len(self.nums)):
            if self.visited[i]:
                continue
            path.append(self.nums[i])
            self.visited[i] = True
            self.dfs(path)
            path.pop()
            self.visited[i] = False

if __name__ == '__main__':
    res = Solution().permutation(strs="abc")
    print(res)

