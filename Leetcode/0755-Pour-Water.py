from typing import List

class Solution:
    def pourWater(self, heights: List[int], volume: int, k: int) -> List[int]:
        for _ in range(volume):
            mark = k   # where to fall water

            l = k - 1   #   search left
            while l >= 0:
                if heights[l] < heights[mark]:
                    mark = l
                elif  heights[l] > heights[mark]:  
                    break
                l -= 1
            if mark < k:
                heights[mark] += 1
                continue

            r = k + 1  #   search right
            while r < len(heights):
                if heights[r] < heights[mark]:
                    mark = r
                elif heights[r] > heights[mark]:
                    break
                r += 1
            heights[mark] += 1
        return heights