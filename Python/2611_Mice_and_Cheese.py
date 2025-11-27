from typing import List
class Solution:
    def miceAndCheese(self, reward1: List[int], reward2: List[int], k: int) -> int:
        res = 0
        diff = {}

        for i in range(len(reward1)):
            diff[i] = reward1[i] - reward2[i]

        sort_diff = sorted(diff.items(), key=lambda x: x[1], reverse=True)
        for i in range(k):
            index = sort_diff[i][0]
            res += reward1[index]
        for i in range(len(reward1) - k):
            index = sort_diff[i + k][0]
            res += reward2[index]
        return res

if __name__ == '__main__':
    res = Solution().miceAndCheese(reward1 = [2,1], reward2 = [1,2], k = 1)
    print(res)