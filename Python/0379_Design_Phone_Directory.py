class PhoneDirectory:
    def __init__(self, maxNumbers: int):
        self.nums = [True] * maxNumbers

    def get(self) -> int:
        for i in range(len(self.nums)):
            if self.nums[i]:
                self.nums[i] = False
                return i
        return -1

    def check(self, number: int) -> bool:
        return self.nums[number]

    def release(self, number: int) -> None:
        self.nums[number] = True


# Your PhoneDirectory object will be instantiated and called as such:
obj = PhoneDirectory(maxNumbers=3)
param_1 = obj.get()
param_2 = obj.check(number=1)
obj.release(number=1)
