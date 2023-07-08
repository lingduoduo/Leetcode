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


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(
        self, headA: ListNode, headB: ListNode
    ) -> Optional[ListNode]:
        lenA, lenB = 0, 0
        cur = headA
        while cur:  # 求链表A的长度
            cur = cur.next
            lenA += 1
        cur = headB
        while cur:  # 求链表B的长度
            cur = cur.next
            lenB += 1
        curA, curB = headA, headB
        if lenA > lenB:  # 让curB为最长链表的头，lenB为其长度
            curA, curB = curB, curA
            lenA, lenB = lenB, lenA
        for _ in range(lenB - lenA):  # 让curA和curB在同一起点上（末尾位置对齐）
            curB = curB.next
        while curA:  # 遍历curA 和 curB，遇到相同则直接返回
            if curA == curB:
                return curA
            else:
                curA = curA.next
                curB = curB.next
        return None


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
