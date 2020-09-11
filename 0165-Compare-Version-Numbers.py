class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = version1.split('.')
        v2 = version2.split('.')

        max_len = max(len(v1), len(v2))

        for i in range(max_len):
            tmp1, tmp2 = 0, 0
            if i < len(v1):
                tmp1 = int(v1[i])
            if i < len(v2):
                tmp2 = int(v2[i])
            if tmp1 < tmp2:
                return -1
            elif tmp2 < tmp1:
                return 1
        return 0