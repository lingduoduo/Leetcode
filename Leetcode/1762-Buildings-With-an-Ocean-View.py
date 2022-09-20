from typing import List


class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        res = []
        for i in reversed(range(len(heights))):
            if i == len(heights) - 1:
                res.append(i)
            elif heights[res[-1]] < heights[i]:
                res.append(i)
        return res[::-1]

if __name__ == "__main__":
    res = Solution().findBuildings(heights = [4,2,3,1])
    print(res)

    res = Solution().findBuildings(heights = [4,3,2,1])
    print(res)

    res = Solution().findBuildings(heights = [1,3,2,4])
    print(res)