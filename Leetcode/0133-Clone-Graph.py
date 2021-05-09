"""
###Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
    if not node: return None

    stack = []
    d = {}

    stack.append(node)
    node_copy = Node(node.val, [])
    d[node] = node_copy

    while stack:
        node = stack.pop()
        for neighbor in node.neighbors:
            if neighbor not in d:
                d[neighbor] = Node(neighbor.val, [])
                stack.append(neighbor)
            d[node].neighbors.append(d[neighbor])
    return node_copy


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node: return None
        
        hashd = dict()
        node_copy = Node(node.val, [])
        hashd[node] = node_copy
        
        stack = collections.deque()
        stack.append(node)
         
        while stack:
            t = stack.popleft()
            if not t: continue
            for n in t.neighbors:
                if n not in hashd:
                    hashd[n] = Node(n.val, [])
                    stack.append(n)
                hashd[t].neighbors.append(hashd[n])
        return node_copy
        