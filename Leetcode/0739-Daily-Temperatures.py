class Solution:
    def dailyTemperatures(self, T):
        res = [0] * len(T)

        stack = []

        for i in reversed(range(len(T))):
            if stack and T[stack[-1]] > T[i]:
                res[i] = stack[-1] - i
            else:
                while stack and T[stack[-1]] <= T[i]:
                    stack.pop()
                if stack and T[stack[-1]] > T[i]:
                    res[i] = stack[-1] - i
            stack.append(i)

        return res

if __name__ == '__main__':
    T = [73, 74, 75, 71, 69, 72, 76, 73]
    result = Solution().dailyTemperatures(T)
    print(result)

#    [1, 1, 4, 2, 1, 1, 0, 0]