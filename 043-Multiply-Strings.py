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
            nums1.append(10**i * (ord(l1.pop()) - ord('0')))
            i += 1
        i = 0
        while l2:
            nums2.append(10**i * (ord(l2.pop()) - ord('0')))
            i += 1
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                res += nums1[i] * nums2[j]
        return str(res)


if __name__ == '__main__':
    result = Solution().multiply('12', '44')
    print(result)
