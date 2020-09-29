###Definition for singly-linked list.
###class ListNode(object):
###    def __init__(self, x):
###        self.val = x
###        self.next = None


# class Solution(object):
#     def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        ###first method
        ###vals = []
        ###for i in range(len(lists)):
        ###    node = lists[i]
        ###    while node:
        ###        vals.append(node.val)
        ###        node = node.next
        ###vals = sorted(vals)
        #
        ###dummy = ListNode(-1)
        ###curr = dummy
        ###while vals:
        ###    curr.next = ListNode(vals.pop(0))
        ###    curr = curr.next
        ###return dummy.next

# class Solution(object):
#     def mergeKLists(self, lists):        
#         import heapq
        
#         ###heapq.heappush(q, 10)
#         ###heapq.heappush(q, 1)
#         #
#         ###while q:
#         ###    print(heapq.heappop(q))
        
#         head = ListNode(0)
#         curr = head
#         heap = []
#         heapq.heapify(heap)
#         [heapq.heappush(heap, (l.val, i)) for i, l in enumerate(lists) if l]
        
#         while heap:
#             curVal, curIdx = heapq.heappop(heap)
#             curHead = lists[curIdx]
#             curNext = curHead.next
            
#             curr.next = curHead
#             curr.next.next = None
#             curr = curr.next
            
#             if curNext:
#                 lists[curIdx]=curNext
#                 heapq.heappush(heap, (curNext.val, curIdx))

#         return head.next


class Solution(object):
    def mergeKLists(self, lists):  
        import heapq

        stack = []
        heapq.heapify(stack)

        for i in range(len(lists)):
            heapq.heappush(stack, (i, lists[i][0]))

        print(stack)

if __name__ == "__main__":
    numbers = [[1,4,5],[1,3,4],[2,6]]
    result = Solution().mergeKLists(numbers)
    print(result)
