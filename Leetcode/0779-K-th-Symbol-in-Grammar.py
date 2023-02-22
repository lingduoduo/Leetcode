class Solution:
    def kthGrammar(self, N: int, K: int) -> int:
        if K == 1:
            return 0
        if K <= (1 << (N - 2)):
            return self.kthGrammar(N - 1, K)
        else:
            return 1 - self.kthGrammar(N - 1, K - (1 << (N - 2)))


class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if n == 1: return 0
        return (1 - k%2) ^ self.kthGrammar(n-1, (k+1)//2)


class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        return bin(k - 1).count('1') % 2

class Solution:
   def kthGrammar(self, n: int, k: int) -> int:
       def f(n, k):
           if n == 1:
               return 0
           return f(n - 1, k // 2) if k % 2 == 0 else 1 - f(n - 1, k // 2)
       k -= 1
       return f(n, k)


if __name__ == '__main__':
    res = Solution().kthGrammar(N=6, K=5)
    print(res)
