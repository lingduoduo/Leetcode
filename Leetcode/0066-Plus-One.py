class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        ###carry = 1
        ###for i in range(len(digits) - 1, -1, -1):
        ###    carry += digits[i]
        ###    if carry < 10:
        ###        digits[i] = carry
        ###        return digits
        ###    else:
        ###        carry = 1
        ###        digits[i] = 0
        ###if carry == 1:
        ###    return [1] + digits

        for i in reversed(range(len(digits))):
            if digits[i] == 9:
                digits[i] = 0
            else:
                digits[i] += 1
                return digits

        digits[0] = 1
        digits.append(0)
        return digits


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        for idx, num in enumerate(digits[::-1]):
            digits[idx] = (num + carry) % 10
            carry = (num + carry) // 10
        print(digits)
        if carry == 1:
            digits.append(1)

        return digits[::-1]


if __name__ == "__main__":
    nums = [1, 2, 3]
    # nums = [9, 9, 9, 9]
    result = Solution().plusOne(nums)
    print(result)
