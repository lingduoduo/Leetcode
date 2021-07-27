class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def printList(self):
        pt = self
        valStr = ""
        while pt:
            valStr += "->" + str(pt.val)
            pt = pt.next
        print(valStr)

class Solution:
    def printListFromTailToHead(self, listNode):
        stack = []
        pt = listNode
        while pt:
            stack.append(pt.val)
            pt = pt.next

        dummy = ListNode(-1)
        pt = dummy
        while stack:
            pt.next = ListNode(stack.pop())
            pt = pt.next
        return dummy.next

        


if __name__ == '__main__':
    l1 = ListNode(0)
    l1.next = ListNode(1)
    l1.next.next = ListNode(2)
    res = Solution().printListFromTailToHead(l1)
    res.printList()
