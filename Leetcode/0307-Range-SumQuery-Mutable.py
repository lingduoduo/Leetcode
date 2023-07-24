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
    def __init__(self, nums: List[int]):
        self.nums = [0]
        for num in nums:
            self.nums.append(self.nums[-1] + num)

    def update(self, i: int, val: int) -> None:
        u = val - (self.nums[i + 1] - self.nums[i])
        self.nums[i + 1 :] = list(map(lambda x: x + u, self.nums[i + 1 :]))

    def sumRange(self, i: int, j: int) -> int:
        return self.nums[j + 1] - self.nums[i]


# Segment tree node
class Node:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.tot = 0
        self.left = None
        self.right = None


class NumArray:
    def __init__(self, nums: List[int]):
        def createTree(nums, l, r):
            if l > r:
                return None

            if l == r:
                node = Node(l, r)
                node.tot = nums[l]
                return node

            mid = l + (r - l) // 2
            root = Node(l, r)
            root.left = createTree(nums, l, mid)
            root.right = createTree(nums, mid + 1, r)
            root.tot = root.left.tot + root.right.tot
            return root

        self.root = createTree(nums, 0, len(nums) - 1)

    def update(self, index: int, val: int) -> None:
        def updateVal(root, i, val):
            # Base case. The actual value will be updated in a leaf.
            # The total is then propogated upwards
            if root.start == root.end:
                root.tot = val
                return val

            mid = (root.start + root.end) // 2

            # If the index is less than the mid, that leaf must be in the left subtree
            if i <= mid:
                updateVal(root.left, i, val)

            # Otherwise, the right subtree
            else:
                updateVal(root.right, i, val)

            # Propogate the changes after recursive call returns
            root.tot = root.left.tot + root.right.tot

            return root.tot

        return updateVal(self.root, index, val)

    def sumRange(self, left: int, right: int) -> int:
        def rangeSum(root, i, j):
            # If the range exactly matches the root, we already have the sum
            if root.start == i and root.end == j:
                return root.tot

            mid = (root.start + root.end) // 2

            # If end of the range is less than the mid, the entire interval lies
            # in the left subtree
            if j <= mid:
                return rangeSum(root.left, i, j)

            # If start of the interval is greater than mid, the entire inteval lies
            # in the right subtree
            elif i >= mid + 1:
                return rangeSum(root.right, i, j)

            # Otherwise, the interval is split. So we calculate the sum recursively,
            # by splitting the interval
            else:
                return rangeSum(root.left, i, mid) + rangeSum(root.right, mid + 1, j)

        return rangeSum(self.root, left, right)


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
