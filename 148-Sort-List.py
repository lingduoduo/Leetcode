# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
'''
Input: 4->2->1->3
Output: 1->2->3->4
'''

class Solution:
    def sortList(self, head):
        if not head or not head.next:
            return head
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        mid = slow.next
        slow.next = None
        return self.merge(self.sortList(head), self.sortList(mid))
    
    def merge(self, l1, l2):
        if not l1: return l2
        if not l2: return l1
    
        head = ListNode(0)
        curr = head

        while l1 and l2:
            if l1.val < l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next
        curr.next = l1 if l1 else l2
        return head.next

if __name__ == '__main__':
    list1 = ListNode(4)
    list1.next = ListNode(2)
    list1.next.next = ListNode(1)
    list1.next.next.next = ListNode(3)
    result = Solution().sortList(list1)
    while result:
        print(result.val)
        result = result.next
