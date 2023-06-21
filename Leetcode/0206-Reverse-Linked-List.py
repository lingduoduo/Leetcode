# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        p1 = head
        new_head = self.reverseList(p1.next)
        p2 = p1.next
        p1.next = None
        p2.next = p1
        return new_head


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head:
            return None

        dummy = ListNode(0)
        dummy.next = head

        curr = head
        head = head.next
        curr.next = None
        curr = head

        while curr:
            tmp = curr.next
            curr.next = dummy.next
            dummy.next = curr
            curr = tmp
        return dummy.next


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        post = head.next
        newhead = self.reverseList(post)
        post.next = head
        head.next = None
        return newhead
