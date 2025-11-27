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

class Solution:
    def str2tree(self, s: str) -> Optional[TreeNode]:
        if not s:
            return None
        stack, number = [], ''
        for c in s:
            if c in '()':
                if c == '(' and number:
                    stack.append(TreeNode(number))
                    number = ''
                elif c== ')':
                    if number:
                        node, parent = TreeNode(number), stack[-1]
                        number = ''
                    else:
                        node, parent = stack.pop(), stack[-1]
                    if parent.left:
                        parent.right = node
                    else:
                        parent.left = node
            else:
                number += c
        if number:
            stack = [TreeNode(number)]
        return stack[0]