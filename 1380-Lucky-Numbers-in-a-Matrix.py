class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        rows = []
        cols = []
        
        for row in matrix:
            rows.append(min(row))
        
        for col in zip(*matrix):
            cols.append(max(col))
        
        return list(set(rows) & set(cols))
        