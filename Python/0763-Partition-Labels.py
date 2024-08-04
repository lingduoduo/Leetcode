from typing import List

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_occurrence = {}  # 存储每个字符最后出现的位置
        for i, ch in enumerate(s):
            last_occurrence[ch] = i

        result = []
        start = 0
        end = 0
        for i, ch in enumerate(s):
            end = max(end, last_occurrence[ch])  # 找到当前字符出现的最远位置
            if i == end:  # 如果当前位置是最远位置，表示可以分割出一个区间
                result.append(end - start + 1)
                start = i + 1

        return result

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        d =  defaultdict(list)
        for i, v in enumerate(s):
            if v not in d:
                d[v] = [i, i]
            else:
                d[v][1] = i
        values = sorted(d.values())
        stack = [values[0]]
        for i in range(1, len(values)):
            if values[i][0] > stack[-1][1]:
                stack.append(values[i])
            else:
                stack[-1][1] = max(stack[-1][1], values[i][1])
        res = [v[1] - v[0] + 1 for v in stack]
        return res

if __name__ == "__main__":
    S = "ababcbacadefegdehijhklij"
    result = Solution().partitionLabels(S)
    print(result)
