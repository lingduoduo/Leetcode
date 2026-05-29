from typing import List, Optional
from collections import deque, defaultdict, Counter
import heapq

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class ProductOfNumbers:

    def __init__(self):
        self.prod = [1]
        

    def add(self, num: int) -> None:
        if num == 0:
            self.prod = [1]
        else:
            self.prod.append(self.prod[-1] * num)
        
    def getProduct(self, k: int) -> int:
        if k >= len(self.prod):
            return 0
        else:
            return self[-1] / self.prod[-k-1]

productOfNumbers = ProductOfNumbers()
productOfNumbers.add(3)
productOfNumbers.add(0)



# if __name__ == "__main__":
#     res = Solution().minInsertions(s = "())")
#     print(res)
