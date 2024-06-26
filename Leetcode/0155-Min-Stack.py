class MinStack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.data = []
        self.minval = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.data.append(x)

        if not self.mindata:
            self.minval.append(x)
        else:
            self.minval.append(min(self.getMin(), x))

    def pop(self):
        """
        :rtype: void
        """
        if not self.data:
            return None
        else:
            self.minval.pop()
        return self.data.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.data[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.minval[-1]


class MinStack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        if not self.stack:
            self.stack.append((x, x))
        else:
            self.stack.append((x, min(x, self.stack[-1][1])))

    def pop(self):
        """
        :rtype: void
        """
        self.stack.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1][0]

    def getMin(self):
        """
        :rtype: int
        """
        return self.stack[-1][1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
