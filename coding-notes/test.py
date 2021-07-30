class Solution:
    def print1ToMaxOfNDigits(self, n: int):
        self.res = []

        number = [''] * n
        self.dfs(number, 0)
        return self.res[1:]

    def dfs(self, number, digit):
        if digit == len(number):
            self.res.append(int(''.join(number)))
            return 

        for i in range(10):
            number[digit] = str(i)
            self.dfs(number, digit + 1)

if __name__ == '__main__':
    res = Solution().print1ToMaxOfNDigits(n=2)
    print(res)
