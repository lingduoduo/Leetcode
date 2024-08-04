# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7


class Solution:
    def rand10(self):
        """
        :rtype: int
        """
        while True:
            r1, r2 = rand7(), rand7()
            t = r1 + (r2 - 1) * 7
            if t <= 40:
                return t % 10 + 1

class Solution:
    def rand10(self):
        l = [rand7() for _ in range(10)]
        return sum(l) % 10 + 1
        