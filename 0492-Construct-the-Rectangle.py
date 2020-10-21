import math
class Solution:
    def constructRectangle(self, area: int):
        res = 0
        for i in reversed(range(2, int(math.sqrt(area)+1))):
            if area % i == 0:
                return [i, area//i] if i > area //i  else [area//i, i]
        return [area, 1]
        
if __name__ == '__main__':
    results = Solution().constructRectangle(122122)
    print(results)
