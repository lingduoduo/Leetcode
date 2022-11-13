# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, row: int, col: int) -> int:
#    def dimensions(self) -> list[]:

class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        rows, cols = binaryMatrix.dimensions()

        # Set pointers to the top-right corner.
        current_row = 0
        current_col = cols - 1

        # Repeat the search until it goes off the grid.
        while current_row < rows and current_col >= 0:
            if binaryMatrix.get(current_row, current_col) == 0:
                current_row += 1
            else:
                current_col -= 1

        # If we never left the last column, it must have been all 0's.
        return current_col + 1 if current_col != cols - 1 else -1