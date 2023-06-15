"""
###Definition for a Node.
class Node(object):
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""
if not head:
    return

dummy = Node(0, None, head, None)
stack = []
stack.append(head)
prev = dummy

while stack:
    curr = stack.pop()
    curr.prev = prev
    prev.next = curr

    if curr.next:
        stack.append(curr.next)
        curr.next = None
    if curr.child:
        stack.append(curr.child)
        curr.child = None
    prev = curr

dummy.next.prev = None
return dummy.next
