class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
    #     return self.dfs(num, [])

    # def dfs(self, num, path):
    #     if len(path)>=3 and path[-1] != path[-2] + path[-3]:
    #         return False
    #     if not num and len(path)>=3:
    #         return True

    #     for i in range(len(num)):
    #         curr = num[:i+1]
    #         if (curr[0] == '0' and len(curr) != 1):
    #             continue
    #         if self.dfs(num[i+1:], path+[int(curr)]):
    #             return True
    #     return False


  def isAdditiveNumber(self, num: str) -> bool:
        n = len(num)
    
        def valid(s): return len(s) == 1 or s[0] != '0'

        def additive(s1, s2, right):
            if not valid(s1) or not valid(s2): 
                return False
            
            s3 = str(int(s1) + int(s2))
            
            if right.startswith(s3):
                if right == s3: 
                    return True
                return additive(s2, s3, right[len(s3):])
            return False

        for l1 in range(1, n // 2 + 1):
            for l2 in range(1, n + 1 - l1):
                if additive(num[:l1], num[l1:l1+l2], num[l1+l2:]):
                    return True
        return False
