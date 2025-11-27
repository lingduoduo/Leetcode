from datetime import *


class Solution:
    def nextClosestTime(self, time):
        s = set(time)
        while True:
            time = (datetime.strptime(time, "%H:%M") + timedelta(minutes=1)).strftime(
                "%H:%M"
            )
            if set(time) <= s:
                return time
        return time
