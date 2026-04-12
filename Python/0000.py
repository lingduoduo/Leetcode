from collections import defaultdict
from typing import List
import math
import heapq
import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []

        que = deque([root])

        while que:
            cur = []
            for _ in range(len(que)):
                node = que.popleft()
                cur.append(node.val)
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)
            res.append(cur)
        return res
                
            


 


        


# if __name__ == "__main__":
#     res = Solution().mergeKLists(lists = [[1,4,5],[1,3,4],[2,6]])
#     print(res)
