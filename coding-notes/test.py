class RandomListNode:
    def __init__(self, label):
        self.label = label
        self.next = None
        self.random = None

class Solution:
    def clone(self, head):
        if not head:
            return None

        # 插入新节点
        cur = head
        while cur:
            clone = RandomListNode(cur.label)
            clone.next = cur.next 
            cur.next = clone
            cur = clone.next

        # 建立 random 链接
        cur = head
        while cur:
            clone = cur.next
            if cur.random is not None:
                clone.random = cur.random.next
            cur = clone.next

        # 拆分
        cur = head 
        newhead = cur.next
        while cur.next:
            clone = cur.next 
            cur.next = clone.next
            cur = clone
        return newhead

if __name__ == '__main__':
    head = RandomListNode(1)
    head.next = RandomListNode(2)
    head.next.next = RandomListNode(3)
    head.next.next.next = RandomListNode(4)

    head.random = head.next.next
    head.next.next.next.random = head.next
    
    res = Solution().clone(head)
    p = res
    while p:
        print(["next", p.label])
        if p.random:
            print(["random", p.random.label])
        p = p.next

