class Solution:
    def countAndSay(self, n: int) -> str:
        seq = "1"
        for i in range(n - 1):
            seq = self.getNext(seq)
        return seq

    def getNext(self, seq):
        i, next_seq = 0, ""
        while i < len(seq):
            count = 1
            while i < len(seq) - 1 and seq[i] == seq[i + 1]:
                count += 1
                i += 1
            next_seq += str(count) + seq[i]
            i += 1
        return next_seq


class Solution:
    def countAndSay(self, n: int) -> str:
        res = "1"
        for _ in range(n - 1):
            prev = res[0]
            cnt = 1
            cur = ""
            for chr in res[1:]:
                if prev == chr:
                    cnt += 1
                else:
                    cur += str(cnt) + prev
                    prev = chr
                    cnt = 1
            res = cur + str(cnt) + prev
        return res


if __name__ == "__main__":
    n = 10
    res = Solution().countAndSay(n)
    print(res)
