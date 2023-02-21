class Solution:
    def compress(self, chars) -> int:
        n = len(chars)
        i, count = 0, 1

        for j in range(1, n - 1):
            if j < n and chars[j - 1] == chars[j]:
                count += 1
            else:
                chars[i] = chars[j - 1]
                i += 1
                if count > 1:
                    for cha in str(count):
                        chars[i] = cha
                        i += 1
                count = 1
        return i

from typing import List
class Solution:
    def compress(self, chars: List[str]) -> int:
        i = 0
        res = 0
        while i < len(chars):
            group_length = 1
            while (i + group_length < len(chars)
                   and chars[i + group_length] == chars[i]):
                group_length += 1
            chars[res] = chars[i]
            res += 1
            if group_length > 1:
                str_repr = str(group_length)
                chars[res:res + len(str_repr)] = list(str_repr)
                res += len(str_repr)
            i += group_length
        return res


if __name__ == "__main__":
    numbers = ["a", "a", "b", "b", "c", "c", "c"]
    numbers = ["c"]
    numbers = ["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"]
    result = Solution().compress(numbers)
    print(result)
