class Solution:
    def minStickers(self, stickers: List[str], target: str) -> int:
        def get_news(s, sticker):
            ft = defaultdict(int)
            for char in sticker:
                ft[char] += 1
            res = []
            for char in s:
                if char in ft:
                    ft[char] -= 1
                    if ft[char] == 0:
                        del ft[char]
                else:
                    res.append(char)
            return "".join(res)

        from collections import defaultdict, deque

        queue = deque()
        queue.append(target)
        visited = set()
        visited.add(target)
        level = 1
        while queue:
            for _ in range(len(queue)):
                curr_s = queue.popleft()
                for sticker in stickers:
                    new_s = get_news(curr_s, sticker)
                    if len(new_s) == 0:
                        return level
                    if new_s in visited:
                        continue
                    visited.add(new_s)
                    queue.append(new_s)
            level += 1
        return -1
