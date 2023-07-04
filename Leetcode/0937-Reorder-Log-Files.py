class Solution(object):
    def reorderLogFiles(self, logs):
        letters = []
        nums = []
        for log in logs:
            logsplit = log.split(" ")
            if logsplit[1].isalpha():
                letters.append((" ".join(logsplit[1:]), logsplit[0]))
            else:
                nums.append(log)
        letters.sort()
        return [letter[1] + " " + letter[0] for letter in letters] + nums


if __name__ == "__main__":
    logs = ["a1 9 2 3 1", "g1 act car", "zo4 4 7", "ab1 off key dog", "a8 act zoo"]
    result = Solution().reorderLogFiles(logs)
    print(result)
