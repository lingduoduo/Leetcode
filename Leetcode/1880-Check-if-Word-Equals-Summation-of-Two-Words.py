class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        l1 = ''.join([str(ord(c) - ord('a')) for c in firstWord])
        l2 = ''.join([str(ord(c) - ord('a')) for c in secondWord])
        l3 = ''.join([str(ord(c) - ord('a')) for c in targetWord])
        return int(l1) + int(l2) == int(l3)

if __name__ == '__main__':
    res = Solution().isSumEqual(firstWord="acb", secondWord="cba", targetWord="cdb")
    print(res)