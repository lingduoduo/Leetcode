class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if len(words) == 0:
            return []
        wordsDict = {}
        for word in words:  # 统计每个单词出现的个数
            if word not in wordsDict:
                wordsDict[word] = 1
            else:
                wordsDict[word] += 1

        n, m, k = len(s), len(words[0]), len(words)  # n, m, k 分别表示，字符串的长度，单词的长度，单词的个数
        res = []

        for i in range(n - m * k + 1):  # 选择一个区间或者窗口
            j = 0
            cur_dict = {}

            while j < k:
                word = s[i + m * j : i + m * j + m]  # 区间内选择一个单词
                if word not in wordsDict:  # 出现不存在的单词，直接结束本此区间
                    break
                if word not in cur_dict:
                    cur_dict[word] = 1
                else:
                    cur_dict[word] += 1
                if cur_dict[word] > wordsDict[word]:  # 某个单词大于所需，则直接结束本此区间
                    break
                j += 1  # 单词数加一
            if j == k:
                res.append(i)  # 记录起始位置

        return res
