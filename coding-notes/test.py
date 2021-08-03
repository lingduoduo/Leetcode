class ListNode(object):
    def __init__(self, val):
        self.val = val
        self.next = None

class Solution:
    def ReverseList(self, head):
        dummy = ListNode(-1)

        while head:
            post = head.next
            head.next = dummy.next
            dummy.next = head
            head = post
        return dummy.next

if __name__ == '__main__':
    root = ListNode(1)
    p = root
    nums = [2, 3, 4, 5, 6]
    for num in nums:
        p.next = ListNode(num)
        p = p.next

    res = Solution().ReverseList(root)
    while res:
        print(res.val)
        res = res.next


# public ListNode ReverseList(ListNode head) {
#     if (head == null || head.next == null)
#         return head;
#     ListNode next = head.next;
#     head.next = null;
#     ListNode newHead = ReverseList(next);
#     next.next = head;
#     return newHead;