class MyCircularQueue:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        """
        self.capacity = k
        self.que = []
        self.cur = 0

    def enQueue(self, value: int) -> bool:
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        """
        if self.cur < self.capacity:
            self.que.append(value)
            self.cur += 1
            return True 
        else:
            return False 

    def deQueue(self) -> bool:
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        """
        if self.cur > 0:
            self.que.pop(0)
            self.cur -= 1
            return True
        else:
            return False

        

    def Front(self) -> int:
        """
        Get the front item from the queue.
        """
        if self.cur > 0:
            return self.que[0]
        else:
            return -1
        

    def Rear(self) -> int:
        """
        Get the last item from the queue.
        """
        if self.cur > 0:
            return self.que[-1]
        else:
            return -1
        

    def isEmpty(self) -> bool:
        """
        Checks whether the circular queue is empty or not.
        """
        if self.cur == 0:
            return True
        else:
            return False

    def isFull(self) -> bool:
        """
        Checks whether the circular queue is full or not.
        """
        if self.cur == self.capacity:
            return True
        else:
            return False


from threading import Lock

class MyCircularQueue:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        """
        self.queue = [0]*k
        self.headIndex = 0
        self.count = 0
        self.capacity = k
        # the additional attribute to protect the access of our queue
        self.queueLock = Lock()

    def enQueue(self, value: int) -> bool:
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        """
        # automatically acquire the lock when entering the block
        with self.queueLock:
            if self.count == self.capacity:
                return False
            self.queue[(self.headIndex + self.count) % self.capacity] = value
            self.count += 1
        # automatically release the lock when leaving the block
        return True
    def deQueue(self) -> bool:
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        """
        if self.count == 0:
            return False
        self.headIndex = (self.headIndex + 1) % self.capacity
        self.count -= 1
        return True

    def Front(self) -> int:
        """
        Get the front item from the queue.
        """
        if self.count == 0:
            return -1
        return self.queue[self.headIndex]

    def Rear(self) -> int:
        """
        Get the last item from the queue.
        """
        # empty queue
        if self.count == 0:
            return -1
        return self.queue[(self.headIndex + self.count - 1) % self.capacity]

    def isEmpty(self) -> bool:
        """
        Checks whether the circular queue is empty or not.
        """
        return self.count == 0

    def isFull(self) -> bool:
        """
        Checks whether the circular queue is full or not.
        """
        return self.count == self.capacity


class MyCircularQueue:

    def __init__(self, k: int):
        self.cap = k
        self.q = [0] * k
        self.ct = 0
        self.head = 0

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        self.q[(self.head + self.ct) % self.cap] = value
        self.ct += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.head = (self.head + 1) % self.cap
        self.ct -= 1
        return True

    def Front(self) -> int:
        if not self.ct:
            return -1
        return self.q[self.head]

    def Rear(self) -> int:
        if not self.ct:
            return -1
        return self.q[(self.head + self.ct - 1) % self.cap]

    def isEmpty(self) -> bool:
        return self.ct == 0

    def isFull(self) -> bool:
        return self.ct == self.cap


if __name__ == '__main__':
    circularQueue = MyCircularQueue(3); 
    # // set the size to be 3
    circularQueue.enQueue(1);  
    # // return true
    circularQueue.enQueue(2);  
    # // return true
    circularQueue.enQueue(3);  
    # // return true
    circularQueue.enQueue(4);  
    # // return false, the queue is full
    circularQueue.Rear();  
    # // return 3
    circularQueue.isFull();  
    # // return true
    circularQueue.deQueue();  
    # // return true
    circularQueue.enQueue(4);  
    # // return true
    circularQueue.Rear();  
    # // return 4
