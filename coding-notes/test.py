class Solution:
    def movingCount(self, m: int, n: int, k: int) -> int:
        visited=[]
        self.cnt = 0
        for i in range(m):
            visited.append([0]*n)

        def dsum(x):
            sumx=0
            while x:
                sumx+=x%10
                x//=10
            return sumx # 数值各位求和

        def bfs(x,y):   
            # 超出边界
            if x < 0 or x >=m or y < 0 or y >= n:
                return 0   

            # 已访问
            if visited[x][y]:
                return 0       

            # 超限
            if dsum(x)+dsum(y) > k:
                return 0

            visited[x][y]=1
            self.cnt += 1
            paths = [[0, -1], [0, 1], [-1, 0], [1, 0]]
            for dx, dy in paths:
                bfs(x + dx, y + dy)

        bfs(0, 0)
        return self.cnt

if __name__ == '__main__':
    res = Solution().movingCount(m=2, n=3, k=1)
    print(res)

    res = Solution().movingCount(m=1, n=3, k=0)
    print(res)