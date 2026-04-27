from collections import defaultdict, deque
from typing import List
import math
import heapq
import bisect


class LogEntry:
#         # BUG WAS HERE: was tokens[0] stored as string
#         # Fix: use float() to parse timestamp as number
#         # Without this, timestamp subtraction returns NaN
#         # causing catchSpeeders() to never detect speeders
    def __init__(self, log_line):
        tokens = log_line.split()

        self.timestamp = float(tokens[0])
        self.license_plate = tokens[1]
        self.booth_type = tokens[3]

        location_str = tokens[2]
        self.location = int(location_str[:-1])

        direction_letter = location_str[-1]
        if direction_letter == 'E':
            self.direction = 'EAST'
        elif direction_letter == 'W':
            self.direction = 'WEST'
        else:
            raise ValueError('Invalid direction letter')

    def __str__(self):
        return (f"<LogEntry timestamp: {self.timestamp} license: {self.license_plate} "
                f"location: {self.location} direction: {self.direction} "
                f"booth type: {self.booth_type}>")


class LogFile:
    def __init__(self, file_contents):
        self.log_entries = []
        lines = file_contents.split('\n')

        for line in lines:
            if line.strip():
                log_entry = LogEntry(line.strip())
                self.log_entries.append(log_entry)

    @property
    def length(self):
        return len(self.log_entries)

    def item(self, index):
        return self.log_entries[index]

    def count_journeys(self):
        count = 0

        for entry in self.log_entries:
            if entry.booth_type == 'ENTRY':
                count += 1

        return count

    def catch_speeders(self):
        result = []
        active_journeys = {}

        for entry in self.log_entries:
            plate = entry.license_plate

            if entry.booth_type == 'ENTRY':
                active_journeys[plate] = [entry.timestamp]

            elif entry.booth_type == 'MAINROAD':
                if plate in active_journeys:
                    active_journeys[plate].append(entry.timestamp)

            elif entry.booth_type == 'EXIT':
                if plate not in active_journeys:
                    continue

                timestamps = active_journeys[plate] + [entry.timestamp]
                del active_journeys[plate]

                fast_segments = 0
                is_speeder = False

                for i in range(len(timestamps) - 1):
                    time_diff = timestamps[i + 1] - timestamps[i]
                    speed = (10 * 3600) / time_diff

                    if speed >= 130:
                        is_speeder = True
                        break

                    if speed >= 120:
                        fast_segments += 1
                        if fast_segments >= 2:
                            is_speeder = True
                            break

                if is_speeder:
                    result.append(plate)

        return result


def test_log_entry():
    log_line = '44776.619 KTB918 310E MAINROAD'
    entry = LogEntry(log_line)

    assert entry.timestamp == 44776.619
    assert entry.license_plate == 'KTB918'
    assert entry.location == 310
    assert entry.direction == 'EAST'
    assert entry.booth_type == 'MAINROAD'

    log_line2 = '52160.132 ABC123 400W ENTRY'
    entry2 = LogEntry(log_line2)

    assert entry2.timestamp == 52160.132
    assert entry2.license_plate == 'ABC123'
    assert entry2.location == 400
    assert entry2.direction == 'WEST'
    assert entry2.booth_type == 'ENTRY'

    print("test_log_entry: OK")


def test_count_journeys():
    sample_log = """90750.191 JOX304 250E ENTRY
91081.684 JOX304 260E MAINROAD
91082.101 THX138 110E ENTRY
91483.251 JOX304 270E MAINROAD
91873.920 THX138 120E MAINROAD
91874.493 JOX304 280E EXIT
91982.102 THX138 290E EXIT
92301.302 THX138 300E ENTRY
92371.302 THX138 310E EXIT"""

    lf = LogFile(sample_log)

    assert lf.count_journeys() == 3
    print("test_count_journeys: OK")


def test_catch_speeders():
    sample_log = """1000.000 TST002 270W ENTRY
1275.000 TST002 260W EXIT
2000.000 TST003 270W ENTRY
2300.000 TST003 260W MAINROAD
2600.000 TST003 250W EXIT
5000.000 TST003 270W ENTRY
5300.000 TST003 260W MAINROAD
5600.000 TST003 250W EXIT"""

    lf = LogFile(sample_log)
    ticket_list = lf.catch_speeders()

    assert len([t for t in ticket_list if t == 'TST002']) == 1
    assert len([t for t in ticket_list if t == 'TST003']) == 2
    assert len(set(ticket_list)) == 2

    print("test_catch_speeders: OK")


if __name__ == '__main__':
    test_log_entry()
    test_count_journeys()
    test_catch_speeders()
    print("\nAll tests passed!")