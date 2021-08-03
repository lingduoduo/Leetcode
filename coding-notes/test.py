class ListNode(object):
    def __init__(self, val):
        self.val = val
        self.next = None

class Solution:
    def merge(self, head1, head2):
        if not head1:
            return head2
        if not head2:
            return head1 

        if head1.val <= head2.val:
            head1.next = self.merge(head1.next, head2)
            return head1
        else:
            head2.next = self.merge(head1, head2.next)
            return head2

if __name__ == '__main__':
    root1 = ListNode(1)
    p = root1
    nums = [2, 3, 4, 5, 6]
    for num in nums:
        p.next = ListNode(num)
        p = p.next

    root2 = ListNode(4)
    p = root2
    nums = [5, 6, 7]
    for num in nums:
        p.next = ListNode(num)
        p = p.next

    res = Solution().merge(root1, root2)
    while res:
        print(res.val)
        res = res.next


# public ListNode Merge(ListNode list1, ListNode list2) {
#     if (list1 == null)
#         return list2;
#     if (list2 == null)
#         return list1;
#     if (list1.val <= list2.val) {
#         list1.next = Merge(list1.next, list2);
#         return list1;
#     } else {
#         list2.next = Merge(list1, list2.next);
#         return list2;
#     }
# }