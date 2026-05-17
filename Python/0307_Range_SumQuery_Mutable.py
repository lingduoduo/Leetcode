from typing import List


class FenwickTree:
    def __init__(self, n):
        self._sums = [0 for _ in range(n + 1)]

    def update(self, i, delta):
        while i < len(self._sums):
            self._sums[i] += delta
            i += i & -i

    def query(self, i):
        s = 0
        while i > 0:
            s += self._sums[i]
        i -= i & -i
        return s


class NumArray(object):
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self._nums = nums
        self._tree = FenwickTree(len(nums))
        for i in range(len(nums)):
            self._tree.update(i + 1, nums[i])

    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: void
        """
        self._tree.update(i + 1, val - self._nums[i])
        self._nusm[i] = val

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self._tree.query(j + 1) - self._tree.query(i)

class NumArray:

    def __init__(self, nums):
        self.n = len(nums)
        self.bit = [0] * (self.n + 1)
        self.arr = nums[:]

        for i in range(self.n):
            self._add(i + 1, nums[i])

    def _add(self, i, delta):
        while i <= self.n:
            self.bit[i] += delta
            i += i & -i

    def update(self, i, val):
        delta = val - self.arr[i]
        self.arr[i] = val
        self._add(i + 1, delta)

    def _query(self, i):
        s = 0
        while i > 0:
            s += self.bit[i]
            i -= i & -i
        return s

    def sumRange(self, l, r):
        return self._query(r + 1) - self._query(l)


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)


if __name__ == "__main__":
    # Your NumArray object will be instantiated and called as such:
    nums = [1, 3, 5]
    obj = NumArray(nums)
    obj.update(1, 2)
    # param_2 = obj.sumRange(i,j)
