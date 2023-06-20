class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        res = 0
        l1 = list(num1)
        l2 = list(num2)

        nums1 = []
        nums2 = []

        i = 0
        while l1:
            nums1.append(10**i * (ord(l1.pop()) - ord("0")))
            i += 1
        i = 0
        while l2:
            nums2.append(10**i * (ord(l2.pop()) - ord("0")))
            i += 1
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                res += nums1[i] * nums2[j]
        return str(res)


class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"
        res = 0
        for i, n1 in enumerate(num2[::-1]):
            pre = 0
            curr = 0
            for j, n2 in enumerate(num1[::-1]):
                multi = (ord(n1) - ord("0")) * (ord(n2) - ord("0"))
                first, second = multi // 10, multi % 10
                curr += (second + pre) * (10**j)
                pre = first
            curr += pre * (10 ** len(num1))
            res += curr * (10**i)
        return str(res)


class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        n1 = len(num1)
        n2 = len(num2)
        res1 = [10 ** (n1 - i - 1) for i in range(n1)]
        res2 = [10 ** (n2 - i - 1) for i in range(n2)]

        res = 0
        for i in range(n1):
            for j in range(n2):
                res += int(num1[i]) * res1[i] * int(num2[j]) * res2[j]
        return str(res)


if __name__ == "__main__":
    result = Solution().multiply("21", "30")
    print(result)
