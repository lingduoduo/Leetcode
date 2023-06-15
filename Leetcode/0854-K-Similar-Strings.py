class Solution:
    def kSimilarity(self, A, B):
        def getSwap(S):  # 用于获取一个节点下可以扩展的所有节点
            for i, c in enumerate(S):  # 找到第一个不相等的字符的-位置-
                if c != B[i]:
                    break
            T = list(S)
            for j in range(i + 1, len(S)):  # 获取所有的可扩展的子节点
                if S[j] == B[i]:  # 找到就交换
                    T[i], T[j] = T[j], T[i]
                    yield "".join(T)  # 返回一个节点
                    T[j], T[i] = T[i], T[j]  # 恢复当前环境，以便寻找下一个可扩展的节点

        queue, cnt = [A], {A: 0}  # 初始化队列，cnt用于记录当前结点已经走了多少步
        while queue:
            S = queue[0]  # 出队
            del queue[0]
            if S == B:
                return cnt[S]  # 结束
            for T in getSwap(S):  # 获取当前节点所有扩展子节点
                if T not in cnt:  # 如果没有出现过，则入队
                    cnt[T] = cnt[S] + 1
                    queue.append(T)


if __name__ == "__main__":
    A, B = "aabc", "abca"
    solu = Solution()
    print(solu.kSimilarity(A, B))
