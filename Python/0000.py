from typing import List, Optional
from collections import defaultdict

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque
class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:

        que = deque([(startGene, 0)])
        seen = {startGene}
        while que:
            node, step = que.popleft()
            if node == endGene:
                return step
            
            for nxt in ["A", "C", "G", "T"]:
                for i in range(len(node)):
                    nei = node[:i] + nxt + node[i+1:]
                    if nei in bank and nei not in seen:
                        que.append((nei, step + 1))
                        seen.add(nei)
        return -1


if __name__ == "__main__":
    res = Solution().minMutation(startGene = "AACCGGTT", endGene = "AACCGGTA", bank = ["AACCGGTA"])
    print(res)