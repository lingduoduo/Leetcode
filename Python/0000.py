from collections import defaultdict
from typing import List

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1)
        dummy.next = head

        p1 = dummy
        p2 = p1.next

        while p2 and p2.next:
                p3 = p2.next
                p1.next, p3.next, p2.next = p3, p2, p3.next
                p1, p2 = p2, p2.next
        return dummy.next

                
if __name__ == "__main__":
    res = Solution().largestRectangleArea(heights = [2,1,5,6,2,3])
    print(res)
