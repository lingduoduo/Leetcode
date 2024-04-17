class ListNode:
    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next


class MyLinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    
    def get(self, index: int) -> int:
        dummy = ListNode(0)
        dummy.next = self.head

        p = dummy.next
        for i in range(index+1):
            if p is None:
                return -1
            p = p.next
        return p.val
    
    def addAtHead(self, val: int) -> None:
        p = ListNode(val, None, self.head)
        if self.head:
            p.prev = self.head.prev
        else:
            self.tail = p
        self.head = p
        self.size += 1
    
    def addAtTail(self, val: int) -> None:
        p = ListNode(val, self.tail, None)
        if self.tail:
            self.tail.next = p
        else:
            self.head = p
        self.tail = p
        self.size += 1
    

    def addAtIndex(self, index: int, val: int) -> None:
        

            
if __name__ == '__main__':
    myLinkedList = MyLinkedList();
    myLinkedList.addAtHead(1);
    myLinkedList.addAtTail(3);
    myLinkedList.addAtIndex(1, 2);    
    myLinkedList.get(1);              
    myLinkedList.deleteAtIndex(1);   
    myLinkedList.get(1);             