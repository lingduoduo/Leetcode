class NestedIterator(object):

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.queue = collections.deque()
        def getAll(nests):
            for nest in nests:
                if nest.isInteger():
                    self.queue.append(nest.getInteger())
                else:
                    getAll(nest.getList())
        getAll(nestedList)

    def next(self):
        """
        :rtype: int
        """
        return self.queue.popleft()

    def hasNext(self):
        """
        :rtype: bool
        """
        return len(self.queue)
    

if __name__ == '__main__':
    vec2d = [[1, 1], 2, [1, 1], 1, 5]
    vec2d = [[1, 1], 2, [1, 1]]
    vec2d = [1, [4, [6]]]
    vec2d = [[[1]]]
    i, v = NestedIterator(vec2d), []
    while i.hasNext():
        v.append(i.next())
    print(v)
