class StringIterator:

    def __init__(self, compressedString: str):
        self.idx = -1
        self.words = ""

        cur = ""
        cnt = 0
        for w in compressedString:
            if w.isdigit():
                cnt = cnt * 10 + int(w)
            else:
                self.words += cur * cnt
                cur = w
                cnt = 0
        if cur:
            self.words += cur * cnt

    def next(self) -> str:
        self.idx += 1
        return self.words[self.idx] if self.idx < len(self.words) else " "


    def hasNext(self) -> bool:
        return self.idx + 1 < len(self.words)


import re
from itertools import accumulate


class StringIterator:

    def __init__(self, compressedString: str):
        self.letter = re.findall(r"\D", compressedString)
        self.number = [int(x) for x in re.findall(r"\d+", compressedString)]
        self.i = self.n = 0

    def next(self) -> str:
        if not self.hasNext(): return " "
        if self.n >= self.number[self.i]:
            self.i += 1
            self.n = 1
        else:
            self.n += 1
        return self.letter[self.i]

    def hasNext(self) -> bool:
        return self.i < len(self.letter) - 1 or self.n < self.number[-1]

# Your StringIterator object will be instantiated and called as such:
# obj = StringIterator(compressedString)
# param_1 = obj.next()
# param_2 = obj.hasNext()