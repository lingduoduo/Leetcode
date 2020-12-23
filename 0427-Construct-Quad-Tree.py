# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        ncnt= len(grid)
        if ncnt == 1:
            return Node(grid[0][0], isLeaf=True, topLeft=None, topRight=None, bottomLeft=None, bottomRight=None)

        def quad(x, y, n):
            if n == 0:
                return None
            all_zeros = True
            all_ones = True
            for i in range(x, n+x):
                for j in range(y, n+y):
                    if grid[i][j] == 0:
                        all_ones = False
                    else:
                        all_zeros = False
            v = 1 if all_ones else 0
            if all_zeros or all_ones:
                return Node(val=v, isLeaf=True, topLeft=None, topRight=None, bottomLeft=None, bottomRight=None)
            else:
                return (Node(val=0, isLeaf=False, 
                    topLeft=quad(x, y, n//2), 
                    topRight=quad(x, y+n//2, n//2), 
                    bottomLeft=quad(x+n//2, y, n//2), 
                    bottomRight=quad(x+n//2, y+n//2, n//2)))
        
        return quad(0, 0, ncnt)


