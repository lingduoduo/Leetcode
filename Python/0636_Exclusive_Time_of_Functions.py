class Solution:
    def exclusiveTime(self, n, logs):
        res = [0] * n
        stack = []
        prevTime = 0
        for log in logs:
            idx, type, time = log.split(":")
            if type == "start":
                if stack:
                    res[stack[-1]] += int(time) - prevTime
                stack.append(int(idx))
                prevTime = int(time)
            else:
                res[stack[-1]] += int(time) - prevTime + 1
                stack.pop()
                prevTime = int(time) + 1
        return res


if __name__ == "__main__":
    n = 2
    logs = ["0:start:2", "0:end:5", "1:start:6", "1:end:6", "0:end:7"]
    results = Solution().exclusiveTime(n, logs)

    # logs = ["0:start:0","0:start:2","0:end:5","1:start:6","1:end:6","0:end:7"]
    # results = Solution().exclusiveTime(n, logs)
    print(results)
