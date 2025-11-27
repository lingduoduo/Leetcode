class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        n = len(num)

        def valid(s):
            return len(s) == 1 or s[0] != "0"

        def additive(s1, s2, right):
            if not valid(s1) or not valid(s2):
                return False

            s3 = str(int(s1) + int(s2))

            if right.startswith(s3):
                if right == s3:
                    return True
                return additive(s2, s3, right[len(s3) :])
            return False

        for l1 in range(1, n // 2 + 1):
            for l2 in range(1, n + 1 - l1):
                if additive(num[:l1], num[l1 : l1 + l2], num[l1 + l2 :]):
                    return True
        return False
