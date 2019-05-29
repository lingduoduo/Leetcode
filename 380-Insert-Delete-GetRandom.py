import random
class RandomizedSet:
    
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.nums = set()
    
    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.nums:
            return False
        else:
            self.nums.add(val)
            return True
    
    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val in self.nums:
            self.nums.remove(val)
            return True
        else:
            return False
    
    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        n = len(self.nums)
        idx = int(random.random()*n)
        return list(self.nums)[idx]

if __name__ == '__main__':
    obj = RandomizedSet()
    param_1 = obj.insert(1)
    print(param_1)
    param_2 = obj.remove(2)
    print(param_2)
    param_3 = obj.getRandom()
    print(param_3)
