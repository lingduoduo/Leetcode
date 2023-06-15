class TwoSum:
    def __init__(self):
        self.nums = []
        self.sums = set()

    def add(self, number: int) -> None:
        if not self.nums:
            self.nums.append(number)
        else:
            for num in self.nums:
                self.sums.add(num + number)
            self.nums.append(number)

    def find(self, value: int) -> bool:
        return value in self.sums


class TwoSum(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.num_counts = {}

    def add(self, number):
        """
        Add the number to an internal data structure..
        :type number: int
        :rtype: None
        """
        if number in self.num_counts:
            self.num_counts[number] += 1
        else:
            self.num_counts[number] = 1

    def find(self, value):
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        :type value: int
        :rtype: bool
        """
        for num in self.num_counts.keys():
            comple = value - num
            if num != comple:
                if comple in self.num_counts:
                    return True
            elif self.num_counts[num] > 1:
                return True

        return False


if __name__ == "__main__":
    obj = TwoSum()
    obj.add(number=1)
    obj.add(number=3)
    obj.add(number=5)
    print(obj.find(4))
    print(obj.find(7))
