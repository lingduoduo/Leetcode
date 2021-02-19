
class MyCircularDeque:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the deque to be k.
        """
        self.k = k
        self.circular = collections.deque([])
        

    def insertFront(self, value: int) -> bool:
        """
        Adds an item at the front of Deque. Return true if the operation is successful.
        """
        if len(self.circular) == self.k:
            return False

        self.circular.appendleft(value)
        return True
        

    def insertLast(self, value: int) -> bool:
        """
        Adds an item at the rear of Deque. Return true if the operation is successful.
        """
        if len(self.circular) == self.k:
            return False

        self.circular.append(value)
        return True
        

    def deleteFront(self) -> bool:
        """
        Deletes an item from the front of Deque. Return true if the operation is successful.
        """
        if len(self.circular) == 0:
            return False

        self.circular.popleft()
        return True
        

    def deleteLast(self) -> bool:
        """
        Deletes an item from the rear of Deque. Return true if the operation is successful.
        """
        if len(self.circular) == 0:
            return False

        self.circular.pop()
        return True
        

    def getFront(self) -> int:
        """
        Get the front item from the deque.
        """
        if len(self.circular) == 0:
            return -1

        return self.circular[0]
        

    def getRear(self) -> int:
        """
        Get the last item from the deque.
        """
        if len(self.circular) == 0:
            return -1

        return self.circular[-1]

    def isEmpty(self) -> bool:
        """
        Checks whether the circular deque is empty or not.
        """
        return len(self.circular) == 0
        

    def isFull(self) -> bool:
        """
        Checks whether the circular deque is full or not.
        """
        return len(self.circular) == self.k
        


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()
