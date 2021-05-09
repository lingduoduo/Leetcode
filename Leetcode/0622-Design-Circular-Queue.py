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
