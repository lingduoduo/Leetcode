class TreeNode:
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = None
        self.right = None
        self.next = None

class Solution:
    def GetNext(self, pNode) -> TreeNode:
        if pNode.right != None:
            pt = pNode.right
            while pt.left:
                pt = pt.left
            return pt
        else:
            pt = pNode
            while pt:
                parent = pt.next
                if parent.left == pt:
                    return parent
                pt = pt.next
        return None


if __name__ == '__main__':
    root = TreeNode(1, None, None, None)
    root.left = TreeNode(2, None, None, root)
    root.right = TreeNode(3, None, None, root)
    root.left.left = TreeNode(4, None, None, root.left)
    root.left.right = TreeNode(5, None, None, root.left)
    res = Solution().GetNext(root.left)
    print(res.val)


