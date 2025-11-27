class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        codes = [
            ".-",
            "-...",
            "-.-.",
            "-..",
            ".",
            "..-.",
            "--.",
            "....",
            "..",
            ".---",
            "-.-",
            ".-..",
            "--",
            "-.",
            "---",
            ".--.",
            "--.-",
            ".-.",
            "...",
            "-",
            "..-",
            "...-",
            ".--",
            "-..-",
            "-.--",
            "--..",
        ]
        d = {}

        for word in words:
            tmp = ""
            for cha in word:
                tmp += codes[ord(cha) - ord("a")]
            if tmp in d:
                d[tmp] += 1
            else:
                d[tmp] = 1
        return len(d.keys())
