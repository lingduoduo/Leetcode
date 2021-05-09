class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res = []  # 记录最终的结果
        cur = []  # 当前正在处理的行，可以容纳的单词列表
        cnt = 0  # 负责记录当前正在处理的行，所有的字符数

        for w in words:
            if cnt + len(w) + len(cur) > maxWidth:  # 超过了一行字符，则不再进行添加单词

                for i in range(maxWidth - cnt):  # 把剩余的空余，填充上空格，从左向右，一边一边的填充
                    cur[i % (len(cur)-1 or 1)] += ' '

                res.append(''.join(cur))  # 添加到 res 列表中
                cur, cnt = [], 0  # 恢复初始值

            cur += [w]  # 添加单词
            cnt += len(w)  # 统计字符数

        res.append(' '.join(cur).ljust(maxWidth))  # 最后一行特殊处理（左对齐），并添加到 res 列表

        return res