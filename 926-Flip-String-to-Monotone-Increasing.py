class Solution(object):
    def minFlipsMonoIncr(self, S):
        """
        :type S: str
        :rtype: int
        """
        left = [0] * len(S)
        right = [0] * len(S)
        
        left[0] = ord(S[0]) - ord('0')
        for i in range(1, len(S)):
            left[i] = left[i - 1] + ord(S[i]) - ord('0')
        
        right[len(S) - 1] = ord('1') - ord(S[len(S) - 1])
        for i in range(len(S) - 2, -1, -1):
            right[i] = right[i + 1] + ord('1') - ord(S[i])
        
        res = min(left[len(S) - 1], right[0])
        for i in range(1, len(S)):
            res = min(res, left[i - 1] + right[i])
        
        return res


if __name__ == "__main__":
    S = "00110"
    S = "010110"
    S = "00011000"
    result = Solution().minFlipsMonoIncr(S)
    print(result)
