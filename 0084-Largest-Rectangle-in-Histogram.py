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