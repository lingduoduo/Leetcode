class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    def reConstructBinaryTree(self, preorder, intorder):
        if len(preorder) == 0 or len(intorder) == 0:
            return None

        root_idx = intorder.index(preorder[0])
        preorder_left = preorder[1:root_idx+1]
        inorder_left = intorder[:root_idx]

        preorder_right = preorder[root_idx+1:]
        inorder_right = intorder[root_idx+1:]

        left = self.reConstructBinaryTree(preorder_left, inorder_left)
        right = self.reConstructBinaryTree(preorder_right, inorder_right)

        return TreeNode(preorder[0], left, right)

if __name__ == '__main__':
    res = Solution().reConstructBinaryTree(preorder=[3, 9, 20, 15, 7], intorder=[9, 3, 15, 20, 7])
    # l1 = ListNode(0)
    # l1.next = ListNode(1)
    # l1.next.next = ListNode(2)
    # res = Solution().printListFromTailToHead(l1)
    # res.printList()


