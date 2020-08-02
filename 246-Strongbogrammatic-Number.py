class Solution(object):
    def isStrobogrammtic(self, num) -> bool:
        d = {'0': '0', '1': "1", "6": "9", "8": "8", "9": "6"}
        n = len(num)
        
        for i in range((n+1)//2):
            if num[i] not in d:
                return False
            elif num[i] != d[num[n-1-i]]:
                return False
        return True
