from typing import List
import collections


class Solution:
    def alienOrder(self, words: List[str]) -> str:
        # create adject matrx of the graph
        adj_list = collections.defaultdict(set)
        # create initial indegrees 0 for all distinct words
        indegrees = {}
        for word in words:
            for c in word:
                if c in indegrees:
                    continue
                indegrees[c] = 0

        # construct the graph and indegrees
        for first_word, second_word in zip(words, words[1:]):
            print(f"{first_word} - {second_word}")
            for c, d in zip(first_word, second_word):
                if c != d:
                    # this line is needed, otherwise the indegrees of d will be repeatedly added
                    if d not in adj_list[c]:
                        adj_list[c].add(d)
                        indegrees[d] += 1
                    break
            # this 'else' will still match with the 'if' inside the for loop, it means if after any zip pairs c and d is not equal, codes in 'else' won't be runned. only when all pairs are equal, then codes in 'else' will be runned. In other words, the 'else' match to the final 'if' of the for loop
            else:
                # check if the second word is a prefix of the first word
                if len(second_word) < len(first_word):
                    return ""

        # pick all nodes with zero indegree and put it into queue
        q = collections.deque()
        for k, v in indegrees.items():
            if v == 0:
                q.append(k)

        # pick off zero indegree nodes level by level,and add to the output
        ans = []
        while q:
            c = q.popleft()
            ans.append(c)
            for d in adj_list[c]:
                indegrees[d] -= 1
                if indegrees[d] == 0:
                    q.append(d)

        # if there are letter that not appear in the output, means there is a cycle in the graph, because on the indegrees of nodes in a cycle will all be non-zero
        if len(ans) < len(indegrees):
            return ""

        return "".join(ans)


if __name__ == "__main__":
    res = Solution().alienOrder(["wrt", "wft", "er", "ett", "rftt"])
    print(res)
