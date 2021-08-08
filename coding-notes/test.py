class Solution:
    def firstNotRepeatingChar(self, s: str) -> int:
        cnts = [0] * 128
        for i in range(len(s)):
            cnts[ord(s[i]) - ord('a')] += 1
            
        for i in range(len(s)):
            if cnts[ord(s[i]) - ord('a')] == 1:
                return s[i]
        return -1

if __name__ == '__main__':
    res = Solution().firstNotRepeatingChar('abacc')
    print(res)


# ```java
# public int FirstNotRepeatingChar(String str) {
#     int[] cnts = new int[128];
#     for (int i = 0; i < str.length(); i++)
#         cnts[str.charAt(i)]++;
#     for (int i = 0; i < str.length(); i++)
#         if (cnts[str.charAt(i)] == 1)
#             return i;
#     return -1;
# }
# ```

# 以上实现的空间复杂度还不是最优的。考虑到只需要找到只出现一次的字符，那么需要统计的次数信息只有 0,1,更大，使用两个比特位就能存储这些信息。
# ```java
# public int FirstNotRepeatingChar2(String str) {
#     BitSet bs1 = new BitSet(128);
#     BitSet bs2 = new BitSet(128);
#     for (char c : str.toCharArray()) {
#         if (!bs1.get(c) && !bs2.get(c))
#             bs1.set(c);     // 0 0 -> 0 1
#         else if (bs1.get(c) && !bs2.get(c))
#             bs2.set(c);     // 0 1 -> 1 1
#     }
#     for (int i = 0; i < str.length(); i++) {
#         char c = str.charAt(i);
#         if (bs1.get(c) && !bs2.get(c))  // 0 1
#             return i;
#     }
#     return -1;
# }
# ```
