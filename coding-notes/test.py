class Solution(object):
    def lastRemaining_Solution(self, n, m):
        if n == 0:
            return -1 
        if n == 1:
            return 0 
        return (self.lastRemaining_Solution(n - 1, m) + m) % n



if __name__ == '__main__':
    res = Solution().lastRemaining_Solution(n = 5, m = 2)
    print(res)

