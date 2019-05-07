class NumArray(object):
    
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums
    
    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return sum(self.nums[i:(j + 1)])


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)

class NumArray(object):
    
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums
    
    def sumPos(self, pos):
        sum = 0
        for x in range(pos + 1):
            sum += self.nums[x]
        return sum
    
    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        if i == 0:
            return self.sumPos(j)
        else:
            return self.sumPos(j) - self.sumPos(i - 1)
