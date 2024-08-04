class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        words = re.findall(r"\w+", paragraph.lower())
        tmp = []
        for word in words:
            if word.lower() not in banned:
                tmp.append(word.lower())
        res = collections.Counter(tmp)
        return res.most_common()[0][0]

        p = re.compile(r"[!?',;.]")
        sub_para = p.sub(" ", paragraph.lower())
        words = sub_para.split(" ")
        words = [word for word in words if word and word not in banned]
        count = collections.Counter(words)
        return count.most_common()[0][0]
