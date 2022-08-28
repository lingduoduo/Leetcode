from typing import List

class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        for i in range(len(letters)):
            if letters[i] > target and i < len(letters) - 1:
                return letters[i]
        return letters[0]

class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        left, right = 0, len(letters)
        while left < right:
            mid = left + (right - left) // 2
            if letters[mid] <= target:
                left = mid + 1
            else:
                right = mid
        return letters[left % len(letters)]

if __name__ == "__main__":
    res = Solution().nextGreatestLetter(letters = ["c","f","j"], target = "a")
    print(res)

    res = Solution().nextGreatestLetter(letters = ["c","f","j"], target = "c")
    print(res)