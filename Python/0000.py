from typing import List, Optional
from collections import deque, defaultdict
import heapq

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key=lambda x: (-x[0], x[1]))
        res = []
        for i, v in enumerate(people):
            _, idx = v
            res = res[:idx] + [people[i]] + res[idx:]
        return res


if __name__ == "__main__":
    print(Solution().reconstructQueue(people = [[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]))