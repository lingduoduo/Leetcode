from typing import List
from collections import defaultdict, deque

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        t = []
        for x, y in zip(position, speed):
            t.append((target - x) /y)
        print(t)



if __name__ == "__main__":
   res = Solution().carFleet(target = 12, position = [10,8,0,5,3], speed = [2,4,1,1,3])
   print(res)