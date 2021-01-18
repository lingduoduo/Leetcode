from typing import List
import collections
class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        res = collections.defaultdict(int)
        for x, y in rectangles:
            res[min(x, y)] += 1

        res = sorted(res.items(), key=lambda x: x[0])
        return res[-1][1]
       

# class Solution:
#     def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
#         res = []
#         for x, y in rectangles:
#             res.append(min(x, y))

#         return sum([1 if num == max(res) else 0 for num in res])

if __name__ == '__main__':
	rectangles = [[5,8],[3,9],[5,12],[16,5]]
	res = Solution().countGoodRectangles(rectangles)
	print(res)