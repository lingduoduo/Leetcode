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
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
    ###first try
    ###head = ListNode(0)
    ###current = head
    ###carry = 0
    #
    ###while l1 or l2:
    ###    val = carry
    ###    if l1:
    ###        val += l1.val
    ###        l1 = l1.next
    ###    if l2:
    ###        val += l2.val
    ###        l2 = l2.next
    ###    carry, val = val / 10, val % 10
    ###    current.next = ListNode(val)
    ###    current = current.next
    ###if carry == 1:
    ###    current.next = ListNode(1)
    ###return head.next

 class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:   
    ###second try
      dummy = tail = ListNode(0)
      carry = 0
      tmp = 0
      while l1 or l2 or carry>0:
         if l1:
             tmp += l1.val
             l1 = l1.next
         if l2:
             tmp += l2.val
             l2 = l2.next
         if carry>0:
             tmp += 1
             carry = 0
         if tmp>=10:
             carry = 1
             tmp -= 10
         tail.next = ListNode(tmp)
         tmp = 0
         tail = tail.next
      if carry>0:
         tail.next = ListNode(carry)
         tail = tail.next
      return dummy.next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
    dummy = tail = ListNode(0)
    s = 0
    while l1 or l2 or s:
        s += (l1.val if l1 else 0) + (l2.val if l2 else 0)
        tail.next = ListNode( s % 10 )
        tail = tail.next
        s //= 10
        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None
    return dummy.next
    

if __name__ == "__main__":
    l1 = ListNode(0)
    pt = l1
    pt.next = ListNode(2)
    pt = pt.next
    pt.next = ListNode(4)
    pt = pt.next
    pt.next = ListNode(3)

    l2 = ListNode(0)
    pt = l2
    pt.next = ListNode(5)
    pt = pt.next
    pt.next = ListNode(6)
    pt = pt.next
    pt.next = ListNode(4)

    result = addTwoNumbers(l1, l2)
    l1.printList()
    l2.printList()
    result.printList()

###class Solution(object):
###    def addTwoNumbers(self, l1, l2):
###        """
###        :type l1: ListNode
###        :type l2: ListNode
###        :rtype: ListNode
###        """
###        head = ListNode(0)
###        answer = head
###        carry = 0
###        while l1 and l2:
###            add = l1.val + l2.val + carry
###            carry = 1 if add >= 10 else 0
###            head.next = ListNode(add % 10)
###            head = head.next
###            l1, l2 = l1.next, l2.next
###        l = l1 if l1 else l2
###        while l:
###            add = l.val + carry
###            carry = 1 if add >= 10 else 0
###            head.next = ListNode(add % 10)
###            head = head.next
###            l = l.next
###        if carry:
###            head.next = ListNode(1)
###        return answer.next
