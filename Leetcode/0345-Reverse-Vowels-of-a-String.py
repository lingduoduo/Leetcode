class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        ###l1 = list(s)
        ###pos = []
        ###l2 = []
        ###for i in range(len(l1)):
        ###    if l1[i] in ['i', 'e', 'a', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:
        ###        pos.append(i)
        ###        l2.append(l1[i])
        ###l2 = l2[::-1]
        ###for i in range(len(l2)):
        ###    l1[pos[i]] = l2[i]
        ###return ''.join(l1)
        strs = [cha for cha in s]
        ref = ['i', 'e', 'a', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        left = 0
        right = len(s) - 1
        while left < right:
            while strs[left] not in ref and left < right:
                left += 1
            while strs[right] not in ref and left < right:
                right -= 1
            strs[left], strs[right] = strs[right], strs[left]
            left += 1
            right -= 1
        return ''.join(strs)


if __name__ == "__main__":
    ###s="hello"
    ###result = Solution().reverseVowels(s)
    ###print(result)
    s = "aA"
    result = Solution().reverseVowels(s)
    print(result)
