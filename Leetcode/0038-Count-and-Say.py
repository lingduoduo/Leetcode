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
        current_string = "1"
        for _ in range(n - 1):
            next_string = ""
            j = 0
            k = 0
            while j < len(current_string):
                while (
                    k < len(current_string) and current_string[k] == current_string[j]
                ):
                    k += 1
                next_string += str(k - j) + current_string[j]
                j = k
            current_string = next_string

        return current_string


if __name__ == "__main__":
    n = 10
    res = Solution().countAndSay(n)
    print(res)
