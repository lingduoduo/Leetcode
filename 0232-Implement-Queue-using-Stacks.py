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

###Your MyQueue object will be instantiated and called as such:
###obj = MyQueue()
###obj.push(x)
###param_2 = obj.pop()
###param_3 = obj.peek()
###param_4 = obj.empty()
