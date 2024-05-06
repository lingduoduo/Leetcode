class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        m=len(grid)
        n=len(grid[0])
        arr=deque([])
        numOfKeys=0
        keys={'a':0,'b':1,'c':2,'d':3,'e':4,'f':5}
        locks={'A':0,'B':1,'C':2,'D':3,'E':4,'F':5}
        for i in range(m):
            for j in range(n):
                if grid[i][j]=='@':
                    arr.append((i,j,0,0))
                elif grid[i][j] in keys:
                    numOfKeys+=1

