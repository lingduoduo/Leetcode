from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        stack = []
        i = 0
        while i < len(traversal):
            # calculate the depth
            depth = 0
            while traversal[i] == '-':
                depth += 1
                i += 1

            # calculate the value
            value = ''
            while i < len(traversal) and traversal[i] != '-':
                value += traversal[i]
                i += 1
            value = int(value)

            # create the node
            curr_node = TreeNode(val=value)

            # move to curr_level
            while stack and len(stack) > depth:
                stack.pop()

            # add
            if stack:
                # left child
                if stack[-1].left is None:
                    stack[-1].left = curr_node
                # right child
                else:
                    stack[-1].right = curr_node

            stack.append(curr_node)
        return stack[0]