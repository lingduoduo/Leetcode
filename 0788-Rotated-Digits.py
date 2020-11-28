class Solution:
    def rotatedDigits(self, N: int) -> int:
        res = 0
        for i in range(1, N+1):
            nums = list(str(i))
            new = []
            for num in nums:
                if num in ['3', '4', '7']:
                    break
                elif num == '2':
                    new.append('5')
                elif num == '5':
                    new.append('2')
                elif num == '6':
                    new.append('9')
                elif num == '9':
                    new.append('6')
                else:
                    new.append(num)
            if len(new)==len(nums) and nums != new:
                res+=1
        return res


if __name__ == '__main__':
    res = Solution().rotatedDigits(11)
    print(res)