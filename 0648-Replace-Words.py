class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        rootset = set(dictionary)

        def replace(word):
            for i in range(len(word)):
                if word[:i] in rootset:
                    return word[:i]
            return word

        return ''.join(map(replace, sentence.split()))


