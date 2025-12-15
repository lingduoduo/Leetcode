from typing import List, Optional


class NestedInteger:
    def __init__(self, value=None):
        """
        If value is not specified, initializes an empty list.
        Otherwise initializes a single integer equal to value.
        """
        if value is None:
            self._integer = None
            self._list = []
        else:
            self._integer = value
            self._list = None

    def isInteger(self) -> bool:
        """
        @return True if this NestedInteger holds a single integer,
        rather than a nested list.
        """
        return self._integer is not None

    def add(self, elem: "NestedInteger") -> None:
        """
        Set this NestedInteger to hold a nested list and add a nested integer elem to it.
        """
        if self._list is None:
            self._list = []
            self._integer = None
        self._list.append(elem)

    def setInteger(self, value: int) -> None:
        """
        Set this NestedInteger to hold a single integer equal to value.
        """
        self._integer = value
        self._list = None

    def getInteger(self) -> Optional[int]:
        """
        @return the single integer that this NestedInteger holds,
        or None if it holds a nested list.
        """
        return self._integer

    def getList(self) -> Optional[List["NestedInteger"]]:
        """
        @return the nested list that this NestedInteger holds,
        or None if it holds a single integer.
        """
        return self._list


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