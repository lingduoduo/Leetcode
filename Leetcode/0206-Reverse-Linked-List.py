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

        dummy = ListNode(-1)
        dummy.next = head

        p1 = dummy
        p2 = p1.next
        p3 = p2.next
        p2.next = None

        p2 = p3
        while p2:
            p3 = p2.next
            p2.next = p1.next
            p1.next = p2
            p2 = p3
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


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        cur = head
        pre = None
        while cur:
            post = cur.next  # 保存一下 cur的下一个节点，因为接下来要改变cur->next
            cur.next = pre  # 反转
            # 更新pre、cur指针
            pre = cur
            cur = post
        return pre
