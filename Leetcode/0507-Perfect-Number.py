class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num <= 1: return False
        steps = num //2 + 1
        j = 2
        res = [1]
        while j < math.sqrt(steps)+1:
            if num % j == 0:
                res.append(j)
                res.append(num/j)
            j += 1

        return sum(res) == num

if __name__ == '__main__':
    num =28
    result = Solution().checkPerfectNumber(num)
    print(result)