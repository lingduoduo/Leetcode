class Solution:
    def findSubstringInWraproundString(self, p: str) -> int:
    '''
    key是字符，value是到这个字符可以形成的substring 数量
    '''
        if not p or len(p) == 0:
            return 0 
        count = collections.defaultdict(int)
        pattern = 'zabcdefghijklmnopqrstuvwxyz'
        
        max_length = 1 
        count[p[0]] = 1 
        for i in range(1, len(p)):
            if p[i-1] + p[i] in pattern:
                max_length += 1 
            else:
                max_length = 1 
            count[p[i]] = max(count[p[i]], max_length)
      
        return sum(count.values())


if __name__ == '__main__':
    # p = "aca"
    # p = "cac"
    p = "zab"
    res = Solution().findSubstringInWraproundString(p)
    print(res)