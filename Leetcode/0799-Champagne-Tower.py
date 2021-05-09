class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        first = [poured]
        for i in range(query_row):
            second = [0] * (1+len(first))
            for idx, val in enumerate(first):
                if val <=1 :
                    continue
                second[idx] += (first[idx]-1)/2
                second[idx+1] += (first[idx]-1)/2
            first = second
        return min(first[query_glass], 1)
            