class Solution:
    def leftRotateString(self, s, k):
        if k >= len(s):
            return s

        strs = list(s)
        self.rev(strs, 0, k - 1)
        self.rev(strs, k, len(s) - 1)
        self.rev(strs, 0, len(s) - 1)
        return ''.join(strs)

    def rev(self, chrs, i, j):
        while i < j:
            chrs[i], chrs[j] = chrs[j], chrs[i]
            i += 1
            j -= 1

if __name__ == '__main__':
    res = Solution().leftRotateString(s="abcXYZdef", k=3)
    print(res)
  

# # ```java
# public String LeftRotateString(String str, int n) {
#     if (n >= str.length())
#         return str;
#     char[] chars = str.toCharArray();
#     reverse(chars, 0, n - 1);
#     reverse(chars, n, chars.length - 1);
#     reverse(chars, 0, chars.length - 1);
#     return new String(chars);
# }

# private void reverse(char[] chars, int i, int j) {
#     while (i < j)
#         swap(chars, i++, j--);
# }

# private void swap(char[] chars, int i, int j) {
#     char t = chars[i];
#     chars[i] = chars[j];
#     chars[j] = t;
# }
# # ```