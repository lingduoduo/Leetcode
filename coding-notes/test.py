class Solution:
    def power(self, x:int, n: int) -> int:
        print([x, n])
        if n == 0:
            return 1
        if n == 1:
            return x 

        self.res = 1
        if x < 0:
            self.res = -1
            x = - x
        if n % 2 == 0:
            self.res *= self.power(x, n//2) ** 2
        else:
            self.res *= self.power(x, (n-1)//2) ** 2 
        return self.res

if __name__ == '__main__':
    res = Solution().power(x=-2, n=5)
    print(res)
