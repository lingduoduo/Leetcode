# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if root is None:
            return root
        if root.val > key:
            root.left = self.deleteNode(root.left, key)
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
        else:
            if not root.left:
                return root.right
            if not root.right:
                return root.left
            pt = root.right
            while pt.left:
                pt = pt.left
            root.val = pt.val
            root.right = self.deleteNode(root.right, pt.val)
        return root


class Solution:
    def deleteNode(self, root, key):
        if root is None:
            return root
        if root.val == key:
            if root.left is None and root.right is None:
                return None
            elif root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            else:
                cur = root.right
                while cur.left is not None:
                    cur = cur.left
                cur.left = root.left
                return root.right
        if root.val > key:
            root.left = self.deleteNode(root.left, key)
        if root.val < key:
            root.right = self.deleteNode(root.right, key)
        return root

class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        def deleteOneNode(target: TreeNode) -> TreeNode:
            if target is None:
                return None
            if target.right is None:
                return target.left
            cur = target.right
            while cur.left:
                cur = cur.left
            cur.left = target.left
            return target.right
        
        if root is None:
            return root
        cur = root
        pre = None  
        while cur:
            if cur.val == key:
                break
            pre = cur
            if cur.val > key:
                cur = cur.left
            else:
                cur = cur.right
        if pre is None:  # 如果搜索树只有头结点
            return deleteOneNode(cur)
        # pre 要知道是删左孩子还是右孩子
        if pre.left and pre.left.val == key:
            pre.left = deleteOneNode(cur)
        if pre.right and pre.right.val == key:
            pre.right = deleteOneNode(cur)
        return root