class Solution:
    def countTime(self, time: str) -> int:
        res = 1
        if (time[0] == '?' and time[1] =='?'):
            res *= 24
        elif (time[0] == '?'):
            if (time[1] <= '3'):
                res *= 3
            else: 
                res *= 2
        elif (time[1] == '?'):
            if (time[0] != '2'):
                res *= 10
            else:
                res *= 4
        
        if (time[3] == '?'):
            res *= 6
        if (time[4] == '?'):
            res *= 10

        return res

import re
class Solution:
    def countTime(self, time: str) -> int:
        pattern = time.replace('?', '.')
        return sum(
            re.fullmatch(pattern, f'{hour:02}:{minute:02}') is not None
            for hour in range(24)
            for minute in range(60)
        )