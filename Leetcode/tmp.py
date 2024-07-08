from typing import List, Set, Optional


class Solution:
    def find_res(self, text: str, wordDict: Set[str]) -> List[str]:
        if not text:
            return []

        d = {}
        def dfs(idx: int) -> Optional[List[str]]:
            if idx in d:
                return d[idx]
            if idx == len(text):
                return []

            res = None
            for i in range(idx + 1, len(text) + 1):
                word = text[idx:i]
                if word in wordDict:
                    right = dfs(i)
                    if right is not None:
                        curr = [word] + right
                        if res is None or len(curr) < len(res):
                            res = curr

            d[idx] = res
            return res

        return dfs(0) or []

class Solution:
    def find_res(self, text: str, wordDict: Set[str]) -> List[str]:
        if not text:
            return []

        # Initialize the dp array
        dp = [None] * (len(text) + 1)
        dp[0] = []

        for i in range(1, len(text) + 1):
            for j in range(i):
                if dp[j] is not None and text[j:i] in wordDict:
                    new_split = dp[j] + [text[j:i]]
                    if dp[i] is None or len(new_split) < len(dp[i]):
                        dp[i] = new_split

        return dp[-1] if dp[-1] is not None else []

if __name__ == "__main__":
    res = Solution().find_res('helloworld!', {'he', 'hell', 'low', 'hello', 'world', '!'})
    print(res)  # Output: ['hello', 'world', '!']

    res = Solution().find_res('', {'he', 'hell', 'low', 'hello', 'world', '!'})
    print(res)  # Output: []

    res = Solution().find_res('abcdef', {'he', 'hell', 'low', 'hello', 'world', '!'})
    print(res)  # Output: []
