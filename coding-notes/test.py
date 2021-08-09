class listNode:
    def __init__(self, val):
        self.val = val
        self.next = None 

class Solution:
    def findFirstCommonNode(self, l1, l2):
        p1, p2 = l1, l2
        while p1 != p2:
            p1 = l2 if p1 is None else p1.next
            p2 = l1 if p2 is None else p2.next
        return p1


if __name__ == '__main__':
    l1 = listNode(1)
    l1.next = listNode(2)
    l1.next.next = listNode(3)

    l2 = listNode(1)
    l2.next = listNode(2)
    l2.next.next = l1.next.next

    res = Solution().findFirstCommonNode(l1, l2)
    print(res.val)


#     ListNode l1 = pHead1, l2 = pHead2;
#     while (l1 != l2) {
#         l1 = (l1 == null) ? pHead2 : l1.next;
#         l2 = (l2 == null) ? pHead1 : l2.next;
#     }
#     return l1;
# }