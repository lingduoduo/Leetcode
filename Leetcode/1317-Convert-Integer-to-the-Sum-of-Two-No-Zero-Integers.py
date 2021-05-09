class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        for i in range(n):
            if any(cha == '0'  for cha in str(i) ):
                continue
            j = n-i
            if any(cha == '0' for cha in str(j)):
                continue
            return [i, j]
            