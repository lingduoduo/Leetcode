from collections import defaultdict
from random import choice

class RandomizedCollection:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.d = collections.defaultdict(set)
        self.nums = []        

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        """
        self.d[val].add(len(self.nums))
        self.nums.append(val)
        return len(self.d[val]) == 1

    def remove(self, val: int) -> bool:
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        """
        if not self.d[val]: 
            return False
        remove, last = self.d[val].pop(), self.nums[-1]
        self.nums[remove] = last
        self.d[last].add(remove)
        self.d[last].discard(len(self.nums) - 1)

        self.nums.pop()
        return True
        

    def getRandom(self) -> int:
        """
        Get a random element from the collection.
        """
        import random
        return random.choice(self.nums)
        


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()