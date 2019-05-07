class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        # First try
        # n = len(grid)
        # if n == 0: return 0
        # m = len(grid[0])
        # result = 0
        
        # def dfs(grid, x, y):
        # 	if x<0 or y<0 or x>=n or y>=m or grid[x][y]=='0':
        # 		return
        # 	grid[x][y]='0'
        # 	dfs(grid, x+1, y)
        # 	dfs(grid, x-1, y)
        # 	dfs(grid, x, y+1)
        # 	dfs(grid, x, y-1)
        
        # for i in range(n):
        # 	for j in range(m):
        # 		if grid[i][j] == '1':
        #  		dfs(grid, i, j)
        #  		result += 1
        # return result
        
        # Second Try
        if not grid:
            return 0
        n = len(grid)
        m = len(grid[0])
        res = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == '1':
                    res += 1
                    self.dfs(grid, i, j, n, m)
        return res
    
    def dfs(self, grid, i, j, n, m):
        if i < 0 or j < 0 or i >= n or j >= m or grid[i][j] == '0':
            return
        grid[i][j] = '0'
        self.dfs(grid, i + 1, j, n, m)
        self.dfs(grid, i - 1, j, n, m)
        self.dfs(grid, i, j + 1, n, m)
        self.dfs(grid, i, j - 1, n, m)
