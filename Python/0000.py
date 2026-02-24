import heapq
from typing import List
from collections import defaultdict, deque, Counter
from typing import List, Tuple, Optional


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        if not fast or not fast.next:
            return None
        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next
        return slow

if __name__ == "__main__":
    res = Solution().largestRectangleArea(heights = [2,1,5,6,2,3])
    print(res)