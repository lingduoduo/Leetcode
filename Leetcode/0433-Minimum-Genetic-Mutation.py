class Solution:
    def minMutation(self, start: str, end: str, bank) -> int:
        steps = 0
        stack = [start]

        while stack:
            for i in range(len(stack)):
                node = stack.pop(0)
                if node == end:
                    return steps
                for idx, cha in enumerate(node):
                    for newcha in ["A", "C", "G", "T"]:
                        newchas = node[:idx] + newcha + node[idx+1:]
                        if newchas in bank:
                            stack.append(newchas)
                            bank.remove(newchas)
            steps += 1
        return -1

if __name__ == '__main__':
    # start = "AACCGGTT"
    # end = "AACCGGTA"
    # bank = ["AACCGGTA"]
    # res = Solution().minMutation(start, end, bank)
    # print(res)

    # start = "AACCGGTT"
    # end = "AAACGGTA"
    # bank = ["AACCGGTA", "AACCGCTA", "AAACGGTA"]
    # res = Solution().minMutation(start, end, bank)
    # print(res)

    # start = "AAAAACCC"
    # end = "AACCCCCC"
    # bank = ["AAAACCCC", "AAACCCCC", "AACCCCCC"]
    # res = Solution().minMutation(start, end, bank)
    # print(res)

    start = "AACCTTGG"
    end = "AATTCCGG"
    bank = ["AATTCCGG","AACCTGGG","AACCCCGG","AACCTACC"]
    res = Solution().minMutation(start, end, bank)
    print(res)
        