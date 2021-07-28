class Queue:
    def __init__(self):
        self.instack = []
        self.outstack = []

    def push(self, num):
        self.instack.append(num)

    def pop(self):
        if not self.instack:
            return None
        if len(self.instack) == 1:
            return self.instack.pop()

        for i in range(len(self.instack)-1):
            self.outstack.append(self.instack.pop())
        num = self.instack.pop()
        self.instack = self.outstack[::-1]
        self.outstack = []
        return num

if __name__ == '__main__':
    q = Queue()
    q.push(1)
    q.push(2)
    print(q.pop())
    q.push(3)
    print(q.pop())


