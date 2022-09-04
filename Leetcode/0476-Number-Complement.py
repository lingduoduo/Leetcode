class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        i = 1
        while i <= num:
            i = i << 1
        return (i - 1) ^ num


class Solution:
    def findComplement(self, num: int) -> int:
        if num == 0:
            return 1
        mask = 1 << 30
        while ((num & mask) == 0):
            mask >>= 1
        mask = (mask << 1) - 1
        return num ^ mask