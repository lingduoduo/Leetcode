# class Solution:
#     def buildArray(self, target, n: int):
#         res = []
#         for i in range(1, n+1):
#             if i in target:
#                 res.append("Push")
#             else:
#                 res.append("Push")
#                 res.append("Pop")
        
#         j = len(res) - 1
#         while res and res[-1] == 'Pop':
#             res.pop()
#             res.pop()
#         return res

class Solution:
    def buildArray(self, target, n: int):
        res = []
        cnt = 0
        for i in range(1, n+1):
            if i in target:
                res.append("Push")
                cnt += 1
            else:
                res.append("Push")
                res.append("Pop")
            if len(target) == cnt:
                break
        return res
        
if __name__ == '__main__':
    # target = [1,3]
    # n = 3
    target = [1,2]
    n = 4
    result = Solution().buildArray(target, n)      
    print(result)
                