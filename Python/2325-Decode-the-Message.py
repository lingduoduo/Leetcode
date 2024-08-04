from typing import List


class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        d = {" ": " "}
        cnt = 97
        for cha in key:
            if cha not in d:
                d[cha] = cnt
                cnt += 1
            if len(d) == 27:
                break
        res = [" " if cha == " " else chr(d[cha]) for cha in message]
        return "".join(res)


if __name__ == "__main__":
    res = Solution().decodeMessage(
        key="the quick brown fox jumps over the lazy dog", message="vkbs bs t suepuv"
    )
    print(res)

    res = Solution().decodeMessage(
        key="eljuxhpwnyrdgtqkviszcfmabo", message="zwx hnfx lqantp mnoeius ycgk vcnjrdb"
    )
    print(res)
