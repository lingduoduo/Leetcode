class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        strs = s.split(" ")
        nums = []
        for cha in strs:
            if cha[0] in "0123456789":
                if len(nums) == 0:
                    nums.append(int(cha))
                elif nums[-1] < int(cha):
                    nums.append(int(cha))
                else:
                    return False
        return True

if __name__ == "__main__":
    res = Solution().areNumbersAscending(s="1 box has 3 blue 4 red 6 green and 12 yellow marbles")
    print(res)