from typing import Optional
from collections import deque

class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children if children is not None else []

class Solution:
    def cloneTree(self, root: 'Node') -> 'Node':

        d = {}
        que = deque([root])
        d[root] = Node(root.val)
        while que:
            for _ in range(que):
                node = que.popleft()
                for nei in node.children:
                    d[nei] = Node(nei.val)
                    d[node].children.append(d[nei])
                    que.append(nei)
        return d[root]