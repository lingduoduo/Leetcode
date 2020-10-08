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


class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        if not node: return None

        if node in hashd: return hashd[node]

        node_copy = Node(node.val, [])
        hashd[node] = node_copy

        for neighbor in node.neighbors:
            neighbor_copy = self.dfs(neighbor, hashd)
            if neighbor_copy:
                node_copy.neighbors.append(neighbor_copy)
        return node_copy