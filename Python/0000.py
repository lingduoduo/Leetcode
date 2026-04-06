from collections import defaultdict
from typing import List

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [-1]
        heights.append(0)
        res = 0

        for i, h in enumerate(heights):
            while stack[-1] != -1 and heights[stack[-1]] > h:
                cur = stack.pop()
                height = heights[cur]
                width = i - stack[-1] - 1
                res = max(res, height * width)
            stack.append(i)

        return res

                
if __name__ == "__main__":
    res = Solution().largestRectangleArea(heights = [2,1,5,6,2,3])
    print(res)
