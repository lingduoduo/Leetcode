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


class Solution:
    def minStickers(self, stickers: List[str], target: str) -> int:
        sticker_counts = [Counter(s) for s in stickers]
        def get_word_diff(t, sticker_count):
            ft = Counter(t)
            diff = ft - sticker_count
            # Sort to normalize state, so "abc" and "bca" are treated the same
            return ''.join(ch * diff[ch] for ch in sorted(diff))

        que = deque([''.join(sorted(target))])
        visited = {''.join(sorted(target))}
        step = 0
        while que:
            step += 1
            for _ in range(len(que)):
                curr_t = que.popleft()
                for sticker_count in sticker_counts:
                    # pruning: if sticker cannot reduce curr_t's first char, skip
                    if sticker_count[curr_t[0]] == 0:
                        continue
                    new_t = get_word_diff(curr_t, sticker_count)
                    if not new_t:
                        return step
                    if new_t not in visited:
                        visited.add(new_t)
                        que.append(new_t)
        return -1