import random


class RandomizedSet:
    ###def __init__(self):
    ###    """
    ###    Initialize your data structure here.
    ###    """
    ###    self.nums = set()

    ###def insert(self, val: int) -> bool:
    ###    """
    ###    Inserts a value to the set. Returns true if the set did not already contain the specified element.
    ###    """
    ###    if val in self.nums:
    ###        return False
    ###    else:
    ###        self.nums.add(val)
    ###        return True

    ###def remove(self, val: int) -> bool:
    ###    """
    ###    Removes a value from the set. Returns true if the set contained the specified element.
    ###    """
    ###    if val in self.nums:
    ###        self.nums.remove(val)
    ###        return True
    ###    else:
    ###        return False

    ###def getRandom(self) -> int:
    ###    """
    ###    Get a random element from the set.
    ###    """
    ###    n = len(self.nums)
    ###    idx = int(random.random()*n)
    ###    return list(self.nums)[idx]

    def __init__(self):
        self.nums = list()
        self.dict = dict()

    def insert(self, val: int) -> bool:
        if val not in self.dict:
            self.nums.append(val)
            self.dict[val] = len(self.nums) - 1
            return True
        else:
            return False

    def remove(self, val: int) -> bool:
        if val in self.dict:
            ###use the last value to replace the delete value
            idx = self.dict[val]
            self.nums[idx] = self.nums[-1]
            self.dict[self.nums[-1]] = idx
            self.nums.pop()
            self.dict.pop(val, 0)
            return True
        else:
            return False

        ###if val in self.dict:
        ###    idx, last = self.dict[val], self.nums[-1]
        ###    self.nums[idx] = last
        ###    self.dict[last] = idx
        ###    self.nums.pop()
        ###    self.dict.pop(val, 0)
        ###    return True
        ###return False

    def getRandom(self):
        idx = random.randint(0, len(self.nums) - 1)
        return self.nums[idx]


if __name__ == "__main__":
    obj = RandomizedSet()
    param_1 = obj.insert(1)
    print(param_1)
    param_2 = obj.remove(2)
    print(param_2)
    param_3 = obj.getRandom()
    print(param_3)
