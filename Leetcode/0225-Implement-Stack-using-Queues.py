class MyStack(object):
    
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data = []
    
    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: void
        """
        self.data.append(x)
    
    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        for i in range(len(self.data) - 1):
            self.data.append(self.data.pop(0))
        return self.data.pop(0)
    
    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        for i in range(len(self.data) - 1):
            self.data.append(self.data.pop(0))
        top = self.data.pop(0)
        self.data.append(top)
        return top
    
    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        if len(self.data) == 0:
            return True
        else:
            return False

class MyStack:
    def __init__(self):
        self.que = collections.deque()

    def push(self, x):
        self.que.append(x)
        for i in range(len(self.que) - 1):
            self.que.append(self.que.popleft())

    def pop(self):
        return self.que.popleft()

    def top(self):
        return self.que[0]

    def empty(self):
        return not self.que

