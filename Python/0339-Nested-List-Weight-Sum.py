from typing import List
"""
This is the interface that allows for creating nested lists.
You should not implement it, or speculate about its implementation
"""
class NestedInteger:
    def __init__(self, value=None):
        """
        If value is not specified, initializes an empty list.
        Otherwise initializes a single integer equal to value.
        """
        pass

    def isInteger(self):
        """
        @return True if this NestedInteger holds a single integer, rather than a nested list.
        :rtype bool
        """
        pass

    def add(self, elem):
        """
        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
        :rtype void
        """
        pass

    def setInteger(self, value):
        """
        Set this NestedInteger to hold a single integer equal to value.
        :rtype void
        """
        pass

    def getInteger(self):
        """
        @return the single integer that this NestedInteger holds, if it holds a single integer
        Return None if this NestedInteger holds a nested list
        :rtype int
        """
        pass

    def getList(self):
        """
        @return the nested list that this NestedInteger holds, if it holds a nested list
        Return None if this NestedInteger holds a single integer
        :rtype List[NestedInteger]
        """
        pass


class Solution:
    def depthSum(self, nestedList: List[NestedInteger]) -> int:
        def dfs(nums, depth):
            tot = 0
            for x in nums:
                if x.isInteger():
                    tot += x.getInteger() * depth
                else:
                    tot += dfs(x.getList(), depth + 1) 
            return tot

        return dfs(nestedList, 1)


class Solution:
    def depthSum(self, nestedList: List[NestedInteger]) -> int:
        stack = [(num, 1) for num in nestedList]  # (NestedInteger, depth)
        total = 0

        while stack:
            cur, depth = stack.pop()
            if cur.isInteger():
                total += cur.getInteger() * depth
            else:
                for child in cur.getList():
                    stack.append((child, depth + 1))

        return total