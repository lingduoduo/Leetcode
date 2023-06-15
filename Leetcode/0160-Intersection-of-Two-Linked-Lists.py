###Definition for singly-linked list.
###class ListNode(object):
###    def __init__(self, x):
###        self.val = x
###        self.next = None


# class Solution(object):
# #     def getIntersectionNode(self, headA, headB):
###first try
###stack1 = list()
###stack2 = list()
#
###curr = headA
###while curr:
###    stack1.append(curr)
###    curr = curr.next
###curr = headB
###while curr:
###    stack2.append(curr)
###    curr = curr.next
#
###result = None
###while stack1 and stack2:
###    s1 = stack1.pop()
###    s2 = stack2.pop()
###    if s1 != s2:
###        return result
###    else:
###        result = s1
###return result

###second try
# p1 = headA
# p2 = headB

# while p1!=p2:
#     if not p1:
#         p1 = headB
#     else:
#         p1 = p1.next

#     if not p2:
#         p2 = headA
#     else:
#         p2 = p2.next

# return p1


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        p1 = headA
        p2 = headB
        while p1 != p2:
            if p1:
                p1 = p1.next
            else:
                p1 = headB
            if p2:
                p2 = p2.next
            else:
                p2 = headA
        return p1


if __name__ == "__main__":
    headA = ListNode(4)
    headA.next = ListNode(1)
    headA.next.next = ListNode(8)
    headA.next.next.next = ListNode(4)
    headA.next.next.next.next = ListNode(5)

    headB = ListNode(5)
    headB.next = ListNode(6)
    headB.next.next = ListNode(1)
    headB.next.next.next = headA.next.next

    res = Solution().getIntersectionNode(headA, headB)
    print(res.val)
