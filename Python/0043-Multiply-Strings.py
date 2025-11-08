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


def multiply(num1: str, num2: str) -> str:
    if num1 == "0" or num2 == "0":
        return "0"

    n1, n2 = len(num1), len(num2)
    res = [0] * (n1 + n2)  

    for i in range(n1 - 1, -1, -1):
        d1 = ord(num1[i]) - ord('0')
        for j in range(n2 - 1, -1, -1):
            d2 = ord(num2[j]) - ord('0')
            pos_low = i + j + 1
            pos_high = i + j

            total = res[pos_low] + d1 * d2
            res[pos_low] = total % 10
            res[pos_high] += total // 10

    i = 0
    while i < len(res) and res[i] == 0:
        i += 1

    return ''.join(map(str, res[i:]))



if __name__ == "__main__":
    result = Solution().multiply("21", "30")
    print(result)
