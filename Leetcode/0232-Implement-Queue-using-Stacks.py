class MyQueue(object):
    
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack1 = list()
        self.stack2 = list()
    
    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: None
        """
        self.stack1.append(x)
    
    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        if self.stack2:
            return self.stack2.pop()
        else:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
            return self.stack2.pop()
    
    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        if self.stack2:
            return self.stack2[-1]
        else:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
            return self.stack2[-1]
    
    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return True if not self.stack1 and not self.stack2 else False


class MyQueue:

    def __init__(self):
        self.q = []

    def push(self, x: int) -> None:
        self.q.append(x)

    def pop(self) -> int:
        r = []
        while self.q:
            num = self.q.pop()
            r.append(num)
        r.pop()
        while r:
            self.push(r.pop())
        return num

    def peek(self) -> int:
        l = self.q.copy()
        while l:
            num = l.pop()
        return num

    def empty(self) -> bool:
        return len(self.q) == 0


obj = MyQueue()
obj.push(1)
obj.push(2)
print(obj.q)
param_2 = obj.pop()
print(obj.q)
param_3 = obj.peek()
print(obj.q)
param_4 = obj.empty()
print(obj.q)
