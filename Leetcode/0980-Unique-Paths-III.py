# class Solution(object):
#     def uniquePathsIII(self, grid):
#         """
#         :type grid: List[List[int]]
#         :rtype: int
#         """
#         import copy
#         visit = []
#         count = 0
#         total = len(grid) * len(grid[0])
#         startx,starty = 0,0
#         for i in range(len(grid)):
#             visit.append([0] * len(grid[i]))
#             for j in range(len(grid[i])):
#                 if grid[i][j] == -1:
#                     count += 1
#                 elif grid[i][j] == 1:
#                     startx,starty = i,j
#         visit[startx][starty] = 1
#         queue = [(startx,starty,copy.deepcopy(visit),1)]
#         res = 0
#         while len(queue) > 0:
#             x,y,v,c = queue.pop(0)
#             if grid[x][y] == 2 and c == total - count:
#                 res += 1
#                 continue
#             direction = [(-1,0),(1,0),(0,1),(0,-1)]
#             for i,j in direction:
#                 if x + i >= 0 and x + i < len(grid) and y + j >= 0 and y + j < len(grid[0]) and v[x+i][y+j] == 0 and grid[x+i][y+j] != -1:
#                     v_c = copy.deepcopy(v)
#                     v_c[x+i][y+j] = 1
#                     queue.append((x+i,y+j,v_c,c+1))
#         return res

# class Solution:
#     def uniquePathsIII(self, grid) -> int:
#         count = 1
#         total = len(grid) * len(grid[0])
#         startx,starty = -1,-1
#         self.res = 0
#         for i in range(len(grid)):
#             for j in range(len(grid[0])):
#                 if grid[i][j] == 0:
#                     count += 1
#                 elif grid[i][j] == 1:
#                     startx, starty = i, j
#         print(count)
#         self.dfs(grid, startx, starty, count)
#         return self.res



#     def dfs(self, grid, x, y, n):
#         print([x, y, n])
#         if x<0 or x>=len(grid) or y<0 or y>=len(grid[0]) or grid[x][y]==-1 or n<0:
#             return 0
#         if grid[x][y]==2:
#             if n==0:
#                 self.res += 1
#                 return 
#         grid[x][y]=-1
#         self.dfs(grid, x+1, y, n-1)
#         self.dfs(grid, x-1, y, n-1)
#         self.dfs(grid, x, y-1, n-1)
#         self.dfs(grid, x, y+1, n-1)
#         grid[x][y]=0


class Solution:
    def uniquePathsIII(self, grid) -> int:
        R, C = len(grid), len(grid[0])  # 计算行数和列数

        def neighbors(r, c):
            for nr, nc in ((r-1, c), (r, c-1), (r+1, c), (r, c+1)):
                if 0 <= nr < R and 0 <= nc < C and grid[nr][nc] % 2 == 0:  # 返回可以到达的位置
                    yield nr, nc

        todo = 0
        for r, row in enumerate(grid):
            for c, val in enumerate(row):
                if val != -1: 
                    todo += 1  # 统计不是障碍的点数
                if val == 1:   # 起始位置
                    sr, sc = r, c
                if val == 2:   # 结束位置
                    tr, tc = r, c

        self.ans = 0
        def dfs(r, c, todo):
            print([r, c, todo])
            todo -= 1  # 遍历到一个位置，将当前位置变为-1
            if todo < 0: 
                return
            if r == tr and c == tc:  # 当到达目标位置同时todo为零
                if todo == 0:  
                    self.ans += 1
                return

            grid[r][c] = -1
            for nr, nc in neighbors(r, c):
                dfs(nr, nc, todo)
            grid[r][c] = 0  # 回溯

        dfs(sr, sc, todo)
        return self.ans

if __name__ == '__main__':
    grid = [[1,0,0,0],[0,0,0,0],[0,0,2,-1]]
    result = Solution().uniquePathsIII(grid)
    print(result)




