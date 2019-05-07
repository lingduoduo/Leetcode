# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
# class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """


class NestedIterator(object):
    
    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        # class NestedInteger(object):
        #    def isInteger(self):
        #        """
        #        @return True if this NestedInteger holds a single integer, rather than a nested list.
        #        :rtype bool
        #        """
        #
        #    def getInteger(self):
        #        """
        #        @return the single integer that this NestedInteger holds, if it holds a single integer
        #        Return None if this NestedInteger holds a nested list
        #        :rtype int
        #        """
        #
        #    def getList(self):
        #        """
        #        @return the nested list that this NestedInteger holds, if it holds a nested list
        #        Return None if this NestedInteger holds a single integer
        #        :rtype List[NestedInteger]
        #        """
        nums = []
        
        def getAll(nests, nums):
            for nest in nests:
                if nest.isInteger():
                    nums.append(nest.getInteger())
                else:
                    getAll(nest.getList())
        
        getAll(nestedList, nums)
        
        # nums = []
        # visited = []
        # while nestedList or visited:
        #     while curr:
        #         if type(curr) == int:
        #             nums.append(curr)
        #             if visited:
        #                 curr = visited.pop(0)
        #             elif nestedList:
        #                 curr = nestedList.pop(0)
        #             else:
        #                 break
        #         elif type(curr) == list:
        #             val = curr.pop(0)
        #             visited += curr
        #             curr = val
        
        self.nestedList = nums
        self.idx = 0
    
    def next(self):
        """
        :rtype: int
        """
        self.idx += 1
        return self.nestedList[self.idx - 1]
    
    def hasNext(self):
        """
        :rtype: bool
        """
        if self.idx <= len(self.nestedList) - 1:
            return True
        else:
            return False
    
    # def __init__(self, nestedList):
    #     """
    #     Initialize your data structure here.
    #     :type nestedList: List[NestedInteger]
    #     """
    #     self.nestedList = nestedList
    #     self.row = 0
    #     self.col = 0
    
    # def next(self):
    #     """
    #     :rtype: int
    #     """
    #     if isinstance(self.nestedList[self.row], list):
    #         val = self.nestedList[self.row][self.col]
    #     else:
    #         val = self.nestedList[self.row]
    
    #     try:
    #         if isinstance(self.nestedList[self.row], list) and self.col < len(
    #                 self.nestedList[self.row]) - 1:
    #             self.col += 1
    #         elif self.row < len(self.nestedList) - 1:
    #             self.row += 1
    #             self.col = 0
    #         else:
    #             self.row += 1
    #             self.col += 1
    #     except BaseException:
    #         self.col += 1
    
    #     return val
    
    # def hasNext(self):
    #     """
    #     :rtype: bool
    #     """
    #     try:
    #         if isinstance(self.nestedList[self.row], list) and self.col <= len(
    #                 self.nestedList[self.row]) - 1:
    #             return True
    #         elif self.row <= len(self.nestedList) - 1:
    #             return True
    #         return False
    #     except BaseException:
    #         return False


if __name__ == '__main__':
    vec2d = [[1, 1], 2, [1, 1], 1, 5]
    vec2d = [[1, 1], 2, [1, 1]]
    vec2d = [1, [4, [6]]]
    vec2d = [[[1]]]
    i, v = NestedIterator(vec2d), []
    while i.hasNext():
        v.append(i.next())
    print(v)
