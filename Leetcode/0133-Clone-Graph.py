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
            if not t:
                continue
            for cur in t.neighbors:
                if cur not in hashd:
                    hashd[cur] = Node(cur.val, [])
                    stack.append(cur)
                hashd[t].neighbors.append(hashd[cur])
        return node_copy


class Solution:
    def __init__(self):
        self.visit = {}

    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return node
        if node in self.visit:
            return self.visit[node]
        res = Node(node.val, [])
        self.visit[node] = res
        if node.neighbors:
            res.neighbors = [self.cloneGraph(n) for n in node.neighbors]
        return res