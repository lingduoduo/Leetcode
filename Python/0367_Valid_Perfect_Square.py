class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num == 1:
            return True

        left = 0
        right = num // 2

        while left <= right:
            mid = left + (right - left) // 2
            if mid**2 == num:
                return True
            elif mid**2 < num:
                left = mid + 1
            else:
                right = mid - 1
        return False


class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num == 1:
            return True

        left, right = 1, num // 2 + 1
        ###[left, right)
        while left < right:
            mid = left + (right - left) // 2
            if mid**2 == num:
                return True
            if mid**2 < num:
                left = mid + 1
            else:
                right = mid
        return (left - 1) ** 2 == num
