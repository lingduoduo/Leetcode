class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []
        for i in range(1, n + 1):
            if i % 15 == 0:
                res.append("FizzBuzz")
            elif i % 3 == 0:
                res.append("Fizz")
            elif i % 5 == 0:
                res.append("Buzz")
            else:
                res.append(str(i))
        return res


class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        return [
            "Fizz" * (d % 3 == 0) + "Buzz" * (d % 5 == 0) or f"{d}"
            for d in range(1, n + 1)
        ]
