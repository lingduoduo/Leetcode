from math import gamma


class CombinationIterator:
    def __init__(self, characters: str, combinationLength: int):
        l = len(characters)
        self.count = int(
            gamma(l + 1)
            / gamma(l - combinationLength + 1)
            / gamma(combinationLength + 1)
        )
        self.wg = self.wordgen(characters, combinationLength)

    def next(self) -> str:
        self.count -= 1
        return next(self.wg)

    def hasNext(self) -> bool:
        return self.count > 0

    def wordgen(self, characters, combinationLength):
        if combinationLength == 1:
            yield from characters
        else:
            for i in range(len(characters) - combinationLength + 1):
                yield from (
                    characters[i] + tail
                    for tail in self.wordgen(characters[i + 1 :], combinationLength - 1)
                )


if __name__ == "__main__":
    iterator = CombinationIterator("abc", 2)
    # print(iterator.next())
