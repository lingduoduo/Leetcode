from typing import List

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        res=0
        for i in range(len(heights)):
            h = heights[i]
            for j in range(i, len(heights)):
                if heights[j] < h:
                    h = heights[j]
                if h*(j-i+1) > res:
                    res = h*(j-i+1)
        return res


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = list()
        res = 0
        heights.append(0)
        N = len(heights)
        for i in range(N):
            if not stack or heights[i] > heights[stack[-1]]:
                stack.append(i)
            else:
                while stack and heights[i] <= heights[stack[-1]]:
                    h = heights[stack[-1]]
                    stack.pop()
                    w = i if not stack else i - stack[-1] - 1
                    res = max(res, h * w)
                stack.append(i)
        return res

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(0)
        stack = [-1]
        res = 0
        for i in range(len(heights)):
            while heights[i] < heights[stack[-1]]:
                h = heights[stack.pop()]
                w = i - stack[-1] - 1
                res = max(res, h * w)
            stack.append(i)
        return res

if __name__ == "__main__":
    res = Solution().largestRectangleArea(heights = [2,1,5,6,2,3])
    print(res)