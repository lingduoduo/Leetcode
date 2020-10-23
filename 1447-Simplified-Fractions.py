class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        res = []
        nums = set()
        for i in range(1, n):
            for j in range(i+1, n+1):
                if i/j not in nums:
                    nums.add(i/j)
                    res.append(str(i) + "/" + str(j))
        return res
                
# ["1/2","1/3","1/4","2/3","2/4","3/4"]