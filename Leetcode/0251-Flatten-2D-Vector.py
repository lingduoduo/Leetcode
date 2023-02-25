# Implement an iterator to flatten a 2d vector.

# For example,
# Given 2d vector =

# [
#  [1,2],
#  [3],
#  [4,5,6]
# ]
# By calling next repeatedly until hasNext returns false, the order of
# elements returned by next should be: [1,2,3,4,5,6].


class Vector2D(object):
    
    ###@param vec2d {List[List[int]]}
    def __init__(self, vec2d):
        ###Initialize your data structure here
        self.vec2d = vec2d
        self.row = 0
        self.col = 0
    
    ###@return {int} a next element
    def next(self):
        ###Write your code here
        val = self.vec2d[self.row][self.col]
        
        if self.col < len(self.vec2d[self.row]) - 1:
            self.col += 1
        elif self.row < len(self.vec2d) - 1:
            self.row += 1
            self.col = 0
        else:
            self.col += 1
        return val
    
    ###@return {boolean} true if it has next element
    ###or false
    def hasNext(self):
        ###Write your code here
        if self.col <= len(self.vec2d[self.row]) - 1:
            return True
        elif self.row < len(self.vec2d) - 1:
            return True
        else:
            return False


class Vector2D:

    def __init__(self, a):
        def it():
            for line in a:
                for val in line:
                    self.size -= 1
                    yield val

        self.it = it()
        self.size = sum(len(line) for line in a)

    def next(self):
        return next(self.it)

    def hasNext(self):
        return self.size


if __name__ == '__main__':
    vec2d = [[1, 2], [3], [4, 5, 6]]
    i, v = Vector2D(vec2d), []
    while i.hasNext():
        v.append(i.next())
    print(v)
