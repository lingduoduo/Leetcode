class Solution:
    def findContentChildren(self, g, s) -> int:
        result = 0
        g.sort()
        s.sort()
        j = 0
        for i in range(len(g)):
            while j < len(s) and s[j] < g[i]:
                j += 1
            if j < len(s) and s[j] >= g[i]:
                result += 1
                j += 1
        return result


class Solution:
    def findContentChildren(self, g, s):
        g.sort()  # 将孩子的贪心因子排序
        s.sort()  # 将饼干的尺寸排序
        index = len(s) - 1  # 饼干数组的下标，从最后一个饼干开始
        result = 0  # 满足孩子的数量
        for i in range(len(g) - 1, -1, -1):  # 遍历胃口，从最后一个孩子开始
            if index >= 0 and s[index] >= g[i]:  # 遍历饼干
                result += 1
                index -= 1
        return result


if __name__ == "__main__":
    # g = [1, 2, 3]
    # s = [1, 1]
    # print(Solution().findContentChildren(g, s))

    a = [1, 2, 3]
    b = [1, 2]
    print(Solution().findContentChildren(a, b))
