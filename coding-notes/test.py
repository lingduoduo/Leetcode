from typing import List
class Solution:
    def moreThanHalfNum_Solution(self, numbers):
        # return sorted(numbers)[len(numbers)//2]

        majority = numbers[0]
        cnt = 0
        for num in numbers:
            if num == majority:
                cnt += 1
            else:
                cnt -= 1
            if cnt == 0:
                majority = num
                cnt = 1
        return majority


if __name__ == '__main__':
    res = Solution().moreThanHalfNum_Solution(numbers = [1, 2, 3, 2, 2, 2, 5, 4, 2])
    print(res)
