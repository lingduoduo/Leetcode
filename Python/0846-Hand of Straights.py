from typing import List


class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        while hand:
            start = min(hand)
            print(start)
            for i in range(groupSize):
                if start + i not in hand:
                    return False
                idx = hand.index(start + i)
                hand.pop(idx)
        return True


if __name__ == "__main__":
    res = Solution().isNStraightHand(hand=[1, 2, 3, 6, 2, 3, 4, 7, 8], groupSize=3)
    print(res)
