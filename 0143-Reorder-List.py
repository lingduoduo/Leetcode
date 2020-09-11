###Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def printList(self):
        pt = self
        valStr = ""
        while pt:
            valStr += "->" + str(pt.val)
            pt = pt.next
        print(valStr)

class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        if not head:
            return None

        stack = list()
        curr = head

        while curr:
            stack.append(curr)
            tmp = curr.next
            curr.next = None
            curr = tmp

        dummy = ListNode(-1)
        prev = dummy
        i = 1
        while stack:
            if i%2 == 1:
                node = stack.pop(0)
            else:
                node = stack.pop()
            prev.next = node
            prev = prev.next
            i += 1

        return dummy.next

if __name__ == "__main__":
    l1 = ListNode(1)
    l1.next = ListNode(2)
    l1.next.next = ListNode(3)
    l1.next.next.next = ListNode(4)
    l1.next.next.next.next = ListNode(5)
    l1.next.next.next.next.next = ListNode(56)
    ###l1.printList()
    l2 = Solution().reorderList(l1)
    l2.printList()