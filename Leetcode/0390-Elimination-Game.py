class Solution:
    def lastRemaining(self, n: int) -> int:
        
        # stack = range(1, n+1)
        # flag = 0
        # while len(stack) > 1:
        #     print(stack)
        #     nums = []
        #     for idx, num in enumerate(stack):
        #         if idx % 2 == 1:
        #             nums.append(num)

        #     stack = nums[::-1]
        # return stack[0]

        return  1 if n == 1 else 2*(n//2 + 1 - self.lastRemaining(n//2))


class Solution:
    def lastRemaining(self, n: int) -> int:
        return self.leftToRight(n)

    def leftToRight(self, n):
        if n == 1: return 1
        if n == 2: return 2
        if n & 1 == 1:
            return 2 * self.rightToLeft((n - 1) // 2)
        else:
            return 2 * self.rightToLeft(n // 2)

    def rightToLeft(self, n):
        if n == 1: return 1
        if n == 2: return 1
        if n & 1 == 1:
            return 2 * self.leftToRight((n - 1) // 2)
        else:
            return 2 * self.leftToRight(n // 2) - 1

if __name__ == '__main__':
    n = 9
    res = Solution().lastRemaining(n)
    print(res)
        