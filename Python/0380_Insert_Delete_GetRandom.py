import random

class RandomizedSet:

    def __init__(self):
        self.nums = []
        self.d = {}   

    def insert(self, val: int) -> bool:
        if val in self.d:
            return False
        self.d[val] = len(self.nums)
        self.nums.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.d:
            return False
        
        idx = self.d[val]
        last = self.nums[-1]

        # move last element to idx
        self.nums[idx] = last
        self.pos[last] = idx

        # remove last
        self.nums.pop()
        del self.d[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.nums)


if __name__ == "__main__":
    obj = RandomizedSet()
    param_1 = obj.insert(1)
    print(param_1)
    param_2 = obj.remove(2)
    print(param_2)
    param_3 = obj.getRandom()
    print(param_3)
