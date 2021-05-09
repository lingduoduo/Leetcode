class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ###result = []
        ###for i in range(1, n + 1):
        ###    if i % 15 == 0:
        ###        result.append("FizzBuzz")
        ###    elif i % 3 == 0:
        ###        result.append("Fizz")
        ###    elif i % 5 == 0:
        ###        result.append("Buzz")
        ###    else:
        ###        result.append(str(i))
        ###return result
        #
        ###return [str(i) * (i %
        ###                  3 != 0 and i %
        ###                  5 != 0) + "Fizz" * (i %
        ###                                      3 == 0) + "Buzz" * (i %
        ###                                                          5 == 0) for i in range(1, n + 1)]
        res = []
        for i in range(1, n+1):
            if i % 15 == 0:
                res.append("FizzBuzz")
            elif i % 3 == 0:
                res.append("Fizz")
            elif i % 5 == 0:
                res.append("Buzz")
            else:
                res.append(str(i))
        return res
    