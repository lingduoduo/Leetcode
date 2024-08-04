class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        num_str = list(str(num))
        res = 0
        for i in range(len(num_str) - k + 1):
            sub_num = int("".join(num_str[i : i + k]))
            if sub_num != 0 and num % int(sub_num) == 0:
                res += 1
        return res
