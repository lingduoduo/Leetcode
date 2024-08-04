class Solution(object):
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        S2 = S.replace("-", "").upper()[::-1]
        result = ""
        for i in range(len(S2)):
            result += S2[i]
            if (i + 1) % K == 0 and (i + 1) <> len(S2):
                result += "-"
        return result[::-1]
