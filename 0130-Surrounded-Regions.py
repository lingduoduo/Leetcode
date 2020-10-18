class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        if m==0:
            return 
        
        n = len(board[0])
        
        directions=[(-1,0),(0,1),(1,0),(0,-1)]
        visited=set()

        def dfs(x,y):
            for dx, dy in directions:
                nx,ny=x+dx,y+dy
                if 0<=nx<m and 0<=ny<n and board[nx][ny]=='O' and (nx,ny) not in visited:
                    visited.add((nx,ny))
                    board[nx][ny]='G'
                    dfs(nx, ny)
                
        for x in range(m):
            for y in range(n):
                if (x==0 or x==m-1 or y== 0 or y==n-1) and board[x][y] == 'O' and (x,y) not in visited:
                    board[x][y]='G'
                    visited.add((x,y))
                    dfs(x,y)
                    
        for x in range(m):
            for y in range(n):
                if board[x][y]=='O':
                    board[x][y]='X'
                elif board[x][y]=='G':
                    board[x][y]='O'


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # 如果数组长或宽小于等于2，则不需要替换
        if len(board) <= 2 or len(board[0]) <= 2:
            return
        
        row, col = len(board), len(board[0])
        
        def dfs(i, j):
            """
            深度优先算法，如果符合条件，替换为A并进一步测试，否则停止
            """
            if i < 0 or j < 0 or i >= row or j >= col or board[i][j] != 'O':
                return
            board[i][j] = 'A'
            
            dfs(i - 1, j)
            dfs(i + 1, j)
            dfs(i, j - 1)
            dfs(i, j + 1)
        
        # 从外围开始
        for i in range(row):
            dfs(i, 0)
            dfs(i, col-1)
        
        for j in range(col):
            dfs(0, j)
            dfs(row-1, j)
        
        # 最后完成替换
        for i in range(row):
            for j in range(col):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == 'A':
                    board[i][j] = 'O'
        

