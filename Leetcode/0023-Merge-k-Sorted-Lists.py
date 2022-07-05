# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def mergeKLists(self, lists):
        vals = []
        for i in range(len(lists)):
            node = lists[i]
            while node:
                vals.append(node.val)
                node = node.next
        vals = sorted(vals)

        dummy = ListNode(-1)
        curr = dummy
        while vals:
            curr.next = ListNode(vals.pop(0))
            curr = curr.next
        return dummy.next


class Solution(object):
    def mergeKLists(self, lists):
        import heapq

        ###heapq.heappush(q, 10)
        ###heapq.heappush(q, 1)
        #
        ###while q:
        ###    print(heapq.heappop(q))

        head = ListNode(0)
        curr = head
        heap = []
        heapq.heapify(heap)
        [heapq.heappush(heap, (l.val, i)) for i, l in enumerate(lists) if l]

        while heap:
            curVal, curIdx = heapq.heappop(heap)
            curHead = lists[curIdx]
            curNext = curHead.next

            curr.next = curHead
            curr.next.next = None
            curr = curr.next

            if curNext:
                lists[curIdx] = curNext
                heapq.heappush(heap, (curNext.val, curIdx))

        return head.next


class Solution(object):
    def mergeKLists(self, lists):
        import heapq

        # init heap
        heap = []
        # init dummy head and cursor
        curr = dummy = ListNode(0)
        for idx, element in enumerate(lists):
            # for non-empty linked lists, push the tuple (head node val, head node) onto the heap
            if element:
                heapq.heappush(heap, (element.val, idx, element))
        # due to Python's min heap implementation
        # the heap is now a min heap of head node vals

        while heap:
            # pop the min element (i.e. least node val)
            value, idx, node = heapq.heappop(heap)

            # append the popped value to cursor
            curr.next = ListNode(value)
            # increment cursor and increment node
            curr = curr.next
            node = node.next
            # so that now cursor -> the new node just appended to the tail of the linked list
            # which the dummy head points to
            # and node -> what's remaining of the linked list
            # whose min val was just popped
            # if anything remains, let's do the same thing once again
            # we can see that the top of the heap will always be the min element of all of the
            # remaining lists.
            if node:
                heapq.heappush(heap, (node.val, idx, node))

        return dummy.next


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        q = []
        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(q, (lists[i].val, i))
                lists[i] = lists[i].next

        dummy = ListNode()
        cur = dummy
        while q:
            val, i = heapq.heappop(q)
            cur.next = ListNode(val)
            cur = cur.next
            if lists[i]:
                heapq.heappush(q, (lists[i].val, i))
                lists[i] = lists[i].next
        return dummy.next


if __name__ == "__main__":
    numbers = [[1, 4, 5], [1, 3, 4], [2, 6]]
    result = Solution().mergeKLists(numbers)
    print(result)
