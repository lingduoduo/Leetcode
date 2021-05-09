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

    def __init__(self, nums: List[int]):
        self.nums = [0]
        for num in nums:
            self.nums.append(self.nums[-1]+num) 
            
    def update(self, i: int, val: int) -> None:
        u = val - (self.nums[i+1] - self.nums[i])
        self.nums[i+1:] = list(map(lambda x: x+u, self.nums[i+1:]))

        
    def sumRange(self, i: int, j: int) -> int:
        return self.nums[j+1] - self.nums[i]
        
if __name__ == '__main__':
    # Your NumArray object will be instantiated and called as such:
    nums = [1, 3, 5]
    obj = NumArray(nums)
    obj.update(1, 2)
    # param_2 = obj.sumRange(i,j)
