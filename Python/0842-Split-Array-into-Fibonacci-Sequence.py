from typing import List


class Solution:
    def splitIntoFibonacci(self, S: str) -> List[int]:
        res = []
        self.dfs(S, res, 0)
        return res

    def dfs(self, S, nums, pos):
        if pos == len(S) and len(nums) >= 3:
            return True

        for i in range(pos, len(S)):
            num = int(S[pos : i + 1])
            if (S[pos] == "0" and i > pos) or (num >= 2**31):
                break

            if len(nums) >= 2 and num > nums[-1] + nums[-2]:
                break
            if len(nums) <= 1 or num == nums[-1] + nums[-2]:
                nums.append(int(num))
                if self.dfs(S, nums, i + 1):
                    return True
                nums.pop()
        return False


if __name__ == "__main__":
    S = "123456579"
    res = Solution().splitIntoFibonacci(S)
    print(res)

    S = "11235813"
    res = Solution().splitIntoFibonacci(S)
    print(res)
