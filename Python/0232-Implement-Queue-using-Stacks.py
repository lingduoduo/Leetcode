class MyQueue(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack_in = []
        self.stack_out = []

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: None
        """
        self.stack_in.append(x)

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        if self.empty():
            return None

        if self.stack_out:
            return self.stack_out.pop()
        else:
            for i in range(len(self.stack_in)):
                self.stack_out.append(self.stack_in.pop())
            return self.stack_out.pop()

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        ans = self.pop()
        self.stack_out.append(ans)
        return ans

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return not (self.stack_in or self.stack_out)


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


class MyQueue:
    def __init__(self):
        self.stack_in = []
        self.stack_out = []

    def push(self, x: int) -> None:
        self.stack_in.append(x)

    def pop(self) -> int:
        if self.stack_out:
            return self.stack_out.pop()
        while self.stack_in:
            self.stack_out.append(self.stack_in.pop())
        return self.stack_out.pop()

    def peek(self) -> int:
        num = self.pop()
        self.stack_out.append(num)
        return num

    def empty(self) -> bool:
        return not self.stack_in and not self.stack_out


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
