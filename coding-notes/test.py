class Solution:
    def sum_Solution(self, n : int) -> int:
        return n and (n + self.sum_Solution(n - 1))    

if __name__ == '__main__':
    res = Solution().sum_Solution(n = 100)
    print(res)
