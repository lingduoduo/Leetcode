# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        n = node.next
        node.val = n.val
        node.next = n.next

if __name__ == '__main__':
    root = ListNode(4)
    root.next = ListNode(5)
    root.next.next = ListNode(1)
    root.next.next.next = ListNode(9)
    res = Solution().deleteNode(root, 5)
    
