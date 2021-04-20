class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        self.res=0
        def dfs(x,y,gold):
            self.res = max(self.res, gold)
            dirs = [[-1, 0], [1, 0], [0, 1], [0, -1]]
            for dx, dy in dirs:
                newx = x + dx
                newy = y + dy
                if 0 <= newx < len(grid) and 0 <= newy < len(grid[0]) and grid[newx][newy]!=0 :
                    v = grid[newx][newy]
                    grid[newx][newy]=0
                    dfs(newx, newy, gold+v)
                    grid[newx][newy] = v
        
        for i in range (m):
            for j in range (n):
                if grid[i][j]!=0:
                    x=grid[i][j]
                    grid[i][j]=0
                    dfs(i,j,x)
                    grid[i][j]=x
        return self.res