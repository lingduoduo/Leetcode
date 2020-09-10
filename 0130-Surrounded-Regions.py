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