class Queue:
    def __init__(self):
        self.instack = []
        self.outstack = []

    def push(self, num):
        self.instack.append(num)

    def pop(self):
        if not self.outstack:
            for i in range(len(self.instack)):
                self.outstack.append(self.instack.pop())
        if not self.outstack:
            return None
        else:
            return self.outstack.pop()

if __name__ == '__main__':
    q = Queue()
    q.push(1)
    q.push(2)
    print(q.pop())
    q.push(3)
    print(q.pop())


