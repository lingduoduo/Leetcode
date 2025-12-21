# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7


class Solution:

    def rand10(self):
        while True:
            row = self.rand7() 
            col = self.rand7()
            idx = (row - 1) * 7 + col
            if idx > 40:
                continue
            return (idx - 1) % 10 + 1
            

class Solution:
    def rand10(self):
        l = [rand7() for _ in range(10)]
        return sum(l) % 10 + 1

if __name__ == "__main__":
    res = Solution().rand10()
    print(res)
        