from typing import List, Optional
from collections import defaultdict

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from collections import deque

class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.nums = []
        self.idx = 0

        def dfs(node):
            if not node:
                return
            dfs(node.left)
            self.nums.append(node.val)
            dfs(node.right)
        dfs(root)
        
    def next(self) -> int:
        val = self.nums[self.idx]
        self.idx += 1
        return val
        
    def hasNext(self) -> bool:
        return self.idx < len(self.nums)
        

if __name__ == "__main__":
    res = Solution().canSeePersonsCount(heights = [10,6,8,5,11,9])
    print(res)