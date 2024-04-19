from typing import List
import collections
import heapq

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(0)
        stack = [-1]
        res = 0
        for i, v in enumerate(heights):
            while stack and v < heights[stack[-1]]:
                h = heights[stack[-1]]
                w = i - 1 - stack.pop()
                res = max(res, h*w)
            stack.append(i)
        return res

if __name__ == "__main__":
    res = Solution().largestRectangleArea(heights = [2,1,5,6,2,3]) 
    print(res)

