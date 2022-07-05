# Definition for singly-linked list.
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

class Solution:
    def reorderList(self, head: ListNode) -> None:
    if head and head.next and head.next.next:
        #find mid
        fast, slow = head, head
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        head1 = head
        head2 = slow.next
        slow.next = None

        # reverse linked list head2     
        dummy = ListNode(0)
        dummy.next = head2
        curr = head2.next
        head2.next = None
        while curr:
            temp= curr.next
            curr.next = dummy.next
            dummy.next = curr
            curr = temp
        head2 = dummy.next

        # merge two linked list head1 and head2
        p1 = head1
        p2 = head2
        while p2:
            temp1 = p1.next
            temp2 = p2.next
            p1.next = p2
            p2.next = temp1
            p1 = temp1
            p2 = temp2
            
class Solution:
    def reorderList(self, head: ListNode) -> None:
        if head and head.next and head.next.next:
            
            #find mid
            fast, slow = head, head
            while fast.next and fast.next.next:
                fast = fast.next.next
                slow = slow.next
            head1 = head
            head2 = slow.next
            slow.next = None
            
            # reverse second list
            dummy = ListNode(0)
            dummy.next = head2
            curr = head2.next
            head2.next = None
            
            while curr:
                dummy.next, curr.next, curr = curr, dummy.next, curr.next
            head2 = dummy.next
        
            # merge two linked list head1 and head2
            p1 = head1
            p2 = head2
            while p2:
                p1.next, p2.next, p1, p2 = p2, p1.next, p1.next, p2.next


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