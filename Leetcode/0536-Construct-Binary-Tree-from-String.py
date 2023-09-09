from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def str2tree(self, s: str) -> Optional[TreeNode]:
        num = ""
        stack = []
        for cha in s:
            if cha == "-" or cha.isdigit():
                num += cha
            elif cha == "(":
                if num:
                    node = TreeNode(num)
                    stack.append(node)
                    num = ""
            else:
                if num:
                    node = TreeNode(num)
                    num = ""
                    if stack[-1].left == None:
                        stack[-1].left = node
                    elif stack[-1].right == None:
                        stack[-1].right = node
                else:
                    node = stack.pop()
                    if stack[-1].left == None:
                        stack[-1].left = node
                    else:
                        stack[-1].right = node
        return stack[-1] if stack else TreeNode(num) if s else None
