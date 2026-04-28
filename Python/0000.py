from typing import List, Optional

class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        n = len(heights)
        res = [0] * n
        stack = []

        for i in range(n - 1, -1, -1):
            count = 0
            while stack and stack[-1] < heights[i]:
                stack.pop()
                count += 1

            # see one taller person if exists
            if stack:
                count += 1

            res[i] = count
            stack.append(heights[i])

        return res

if __name__ == "__main__":
    res = Solution().canSeePersonsCount(heights = [10,6,8,5,11,9])
    print(res)