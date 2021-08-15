import collections
class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        import collections
        cnt = collections.Counter(arr)
        for i in sorted(cnt, key=abs):
            if cnt[i] > cnt[2 * i]:
                return False
            cnt[2 * i] -= cnt[i]
        return True
        