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

if __name__ == '__main__':
    n = 9
    res = Solution().lastRemaining(n)
    print(res)
        