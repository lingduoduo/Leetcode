from typing import List


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


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = [0] * n
        stack = []
        for i in range(n):
            while stack and temperatures[stack[-1]] < temperatures[i]:
                preIndex = stack.pop()
                res[preIndex] = i - preIndex
            stack.append(i)
        return res


if __name__ == "__main__":
    T = [73, 74, 75, 71, 69, 72, 76, 73]
    result = Solution().dailyTemperatures(T)
    print(result)

    T = [89, 62, 70, 58, 47, 47, 46, 76, 100, 70]
    result = Solution().dailyTemperatures(T)
    print(result)
