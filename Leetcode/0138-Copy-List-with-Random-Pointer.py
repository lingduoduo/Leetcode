###Definition for singly-linked list with a random pointer.
class Node:
    def init(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random


class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        nodedict = dict()
        dummy = Node(0, None, None)
        nodedict[head] = dummy

        newCurr, curr = dummy, head
        while curr:
            node = Node(curr.val, curr.next, None)
            nodedict[curr] = node
            newCurr.next = node
            newCurr = newCurr.next
            curr = curr.next
        curr = head
        while curr:
            if curr.random:
                nodedict[curr].random = nodedict[curr.random]
            curr = curr.next
        return dummy.next


def copyRandomList(self, head):
    """
    :type head: RandomListNode
    :rtype: RandomListNode
    """
    if not head:
        return None

    # 使用一个字典类型进行拷贝
    res = dict()

    # 数值拷贝
    node = head
    while node:
        res[node] = RandomListNode(node.label)
        node = node.next

    # 设置尾结点
    res[None] = None

    # 进行两个指针的拷贝
    node = head
    while node:
        res[node].next = res[node.next]
        res[node].random = res[node.random]
        node = node.next

    return res[head]


class Solution:
    def copyRandomList(self, head: "Optional[Node]") -> "Optional[Node]":
        if head is None:
            return None

        p = head
        while p:
            clone = Node(p.val)
            clone.next = p.next
            p.next = clone
            p = clone.next

        p1 = head
        while p1:
            p2 = p1.next
            if p1.random:
                p2.random = p1.random.next
            p1 = p2.next

        p1 = head
        newhead = p1.next
        while p1.next:
            p2 = p1.next
            p1.next = p2.next
            p1 = p2
        return newhead


class Solution:
    def __init__(self):
        self.visit = {None: None}

    def copyRandomList(self, head: "Node") -> "Node":
        if head in self.visit:
            return self.visit[head]
        node = Node(head.val, None, None)
        self.visit[head] = node
        node.next = self.copyRandomList(head.next)
        node.random = self.copyRandomList(head.random)
        return node


class Solution:
    def copyRandomList(self, head: "Optional[Node]") -> "Optional[Node]":
        if head is None:
            return None
        d = {}
        p = head
        while p:
            d[p] = Node(p.val, None, None)
            p = p.next
        p = head
        while p:
            if p.next:
                d[p].next = d[p.next]
            if p.random:
                d[p].random = d[p.random]
            p = p.next
        return d[head]
