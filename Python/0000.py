from typing import List
import heapq
from collections import defaultdict


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:

        return [col[::-1] for col in zip(*matrix)]
            

if __name__ == "__main__":
    res = Solution().rotate(matrix = [[1,2,3],[4,5,6],[7,8,9]])
    print(res)
