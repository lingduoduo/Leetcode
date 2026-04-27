### Q1 
找 bug：missing float()
原代码把 timestamp 当成 string 存了。
修复：self.timestamp = float(tokens[0])
否则时间差计算会出错，导致 catch_speeders() 检测不到超速。

完成 count_journeys()
用 license plate 追踪当前是否已经进入高速。
遇到 ENTRY 开始 journey。
遇到 EXIT 并且之前有 entry，就计数 +1。
完成 catch_speeders()
按车牌记录上一条 log。

每次看到同一辆车的新 log，就计算：

speed = distance / time_hours
如果速度超过阈值，就加入 ticket list。

```
class LogEntry:
    def __init__(self, log_line):
        tokens = log_line.split()

        # Bug fix: timestamp must be numeric
        self.timestamp = float(tokens[0])
        self.license_plate = tokens[1]

        location_str = tokens[2]
        self.location = int(location_str[:-1])

        direction_letter = location_str[-1]
        if direction_letter == "E":
            self.direction = "EAST"
        elif direction_letter == "W":
            self.direction = "WEST"
        else:
            raise ValueError("Invalid direction letter")

        self.booth_type = tokens[3]

    def __str__(self):
        return (
            f"<LogEntry timestamp:{self.timestamp} "
            f"license:{self.license_plate} "
            f"location:{self.location} "
            f"direction:{self.direction} "
            f"booth_type:{self.booth_type}>"
        )


class LogFile:
    def __init__(self, file_contents):
        self.log_entries = []

        for line in file_contents.split("\n"):
            line = line.strip()
            if line:
                self.log_entries.append(LogEntry(line))

    @property
    def length(self):
        return len(self.log_entries)

    def __getitem__(self, index):
        return self.log_entries[index]

    def count_journeys(self):
        active = set()
        count = 0

        for entry in self.log_entries:
            plate = entry.license_plate

            if entry.booth_type == "ENTRY":
                active.add(plate)

            elif entry.booth_type == "EXIT":
                if plate in active:
                    count += 1
                    active.remove(plate)

        return count

    def catch_speeders(self, speed_limit=120):
        last_seen = {}
        tickets = []

        for entry in self.log_entries:
            plate = entry.license_plate

            if plate in last_seen:
                prev = last_seen[plate]

                distance = abs(entry.location - prev.location)
                time_hours = (entry.timestamp - prev.timestamp) / 3600

                if time_hours > 0:
                    speed = distance / time_hours
                    if speed >= speed_limit:
                        tickets.append(plate)

            last_seen[plate] = entry

        return tickets
```

### Q2

Course：障碍数量

We are writing software to collect and manage data on how fast racers can complete obstacle courses. An obstacle course is a series of difficult physical challenges (like walls, hurdles, and ponds) that a racer must go through.

Each course consists of multiple obstacles. The software stores how long it takes for racers to finish each obstacle, and provides useful statistics based on those times.

Definitions:

- A "run" is a particular attempt to complete an entire obstacle course
- A "run collection" is a group of runs on a particular course by the user.
- An "obstacle" is a portion of a course. We track how long it takes to finish each portion of the course

For example, here are some times for an obstacle course with four obstacles:

```
Obstacles:    O1  O2  O3  O4
    Run 1:      3   4   5   6    (total: 18 seconds)
    Run 2:      4   4   4   5    (total: 17 seconds)
    Run 3:      4   5   4   6    (total: 19 seconds)
    Run 4:      5   5   3        (13 seconds, but run is incomplete)
    Run 5:      1.      3.  4
                3   4.  3.  5 -> 15
```

All of these runs for one obstacle course (including the incomplete run) make up a
run collection.

1) To begin with, we present you with two tasks:

1-1) Read through and understand the code below. Please take as much time as necessary, and feel free to run the code.

1-2) The test for RunCollection is not passing due to a bug in the code. Make the necessary changes to RunCollection to fix the bug.

2) We would like to implement a new function in RunCollection called "best_of_bests". This is a measure of how fast a run could be if everything went perfectly, and is determined by taking the fastest times for each obstacle across all runs (even incomplete ones) and summing them.

Implement this function, and add a test to verify that it works.

2-2) What other tests would you implement?


3) We would like to implement a new function "chance_of_personal_best". This takes in an in-progress Run object, and determines the chance that this run will be a new personal best, or match the current personal best. This assumes that, for every obstacle after the obstacles already completed in the run, the time to complete that obstacle is uniformly chosen from times to complete that obstacle in all other runs.

We want to do this using simulation. To do this, write a method in RunCollection that takes in an in-progress run and does the following:
* Over 10,000 trials:
  * For each incomplete segment in the current run:
    * Select a time randomly from previous runs (including completed obstacles from incomplete runs)
  * Check if the run, including randomly collected times, is better than or matching
    the current personal best
* Return the chance, over those trials, that the run was a personal best.

The solution should consistently return a solution within .02 of the correct solutions. For example, if there is a .5 (50%) chance of a personal best, the function should return a value between .48 and .52

3-2) Having implemented both best of bests and chance of personal best methods, are there any improvements you'd make to the code?

Run：一次跑（可能 incomplete）
RunCollection：一组 runs

需要完成：

Task 1：修 bug
RunCollection 测试失败 → 找并修

Task 2：实现 best_of_bests()
每个 obstacle 取最小时间（包括 incomplete run）

Task 3：实现 chance_of_personal_best()
Monte Carlo simulation（10000 次）

```
import unittest
from collections import defaultdict
from random import choice


class Course:
    """Data about a particular obstacle course."""

    def __init__(self, title, obstacle_count):
        self.title = title
        self.obstacle_count = obstacle_count

    def __eq__(self, other):
        if not isinstance(other, Course):
            return False
        return (
            self.title == other.title
            and self.obstacle_count == other.obstacle_count
        )


class Run:
    """Data and methods about a single run of a course."""

    def __init__(self, course):
        self.course = course
        self.complete = False
        self.obstacle_times = []

    def add_obstacle_time(self, obstacle_time):
        if self.complete:
            raise ValueError("Cannot add obstacle to complete run")

        self.obstacle_times.append(obstacle_time)

        if len(self.obstacle_times) == self.course.obstacle_count:
            self.complete = True

    def get_run_time(self):
        return sum(self.obstacle_times)


class RunCollection:
    """Collection of runs for one course."""

    def __init__(self, course):
        self.runs = []
        self.course = course

    def get_num_runs(self):
        return len(self.runs)

    def add_run(self, run):
        if run.course != self.course:
            raise ValueError("Run's Course is not the same as the RunCollection's")
        self.runs.append(run)

    def personal_best(self):
        complete_runs = [run.get_run_time() for run in self.runs if run.complete]

        if not complete_runs:
            raise ValueError("No complete runs available")

        return min(complete_runs)

    def obstacle_times(self):
        obstacles = defaultdict(list)

        for run in self.runs:
            for i, obstacle_time in enumerate(run.obstacle_times):
                obstacles[i].append(obstacle_time)

        return obstacles

    def best_of_bests(self):
        obstacles = self.obstacle_times()
        total = 0.0

        for i in range(self.course.obstacle_count):
            if i not in obstacles:
                raise ValueError(f"Missing data for obstacle {i}")

            total += min(obstacles[i])

        return total

    def chance_of_personal_best(self, test_run, trials=10000):
        best = self.personal_best()
        obstacles = self.obstacle_times()

        success = 0

        for _ in range(trials):
            total = test_run.get_run_time()

            for i in range(len(test_run.obstacle_times), self.course.obstacle_count):
                if i not in obstacles:
                    raise ValueError(f"Missing data for obstacle {i}")

                total += choice(obstacles[i])

            if total <= best:
                success += 1

        return success / trials


class TestSuite(unittest.TestCase):

    def make_run_collection(self, course, obstacle_data):
        run_collection = RunCollection(course)

        for run_data in obstacle_data:
            run = Run(course)

            for obstacle_time in run_data:
                run.add_obstacle_time(obstacle_time)

            run_collection.add_run(run)

        return run_collection

    def test_run(self):
        test_course = Course("Test course", 2)
        test_run = Run(test_course)

        test_run.add_obstacle_time(3)
        self.assertFalse(test_run.complete)

        test_run.add_obstacle_time(5)
        self.assertTrue(test_run.complete)

        self.assertEqual(test_run.obstacle_times, [3, 5])
        self.assertEqual(test_run.get_run_time(), 8)

        with self.assertRaises(ValueError):
            test_run.add_obstacle_time(4)

    def test_run_collection(self):
        obstacle_data = [
            [3, 4, 5, 6],
            [4, 4, 4, 5],
            [4, 5, 4, 6],
            [5, 5, 3],
        ]

        test_course = Course("Test course", 4)
        run_collection = self.make_run_collection(test_course, obstacle_data)

        self.assertEqual(run_collection.get_num_runs(), 4)
        self.assertEqual(run_collection.personal_best(), 17)

    def test_best_of_bests(self):
        obstacle_data = [
            [3, 4, 5, 6],
            [4, 4, 4, 5],
            [4, 5, 4, 6],
            [5, 5, 3],
        ]

        test_course = Course("Test course", 4)
        run_collection = self.make_run_collection(test_course, obstacle_data)

        # min O1 = 3
        # min O2 = 4
        # min O3 = 3
        # min O4 = 5
        # total = 15
        self.assertEqual(run_collection.best_of_bests(), 15.0)

    def test_chance_of_personal_best_simple(self):
        obstacle_data = [
            [3, 3, 2],
            [3, 3, 3],
        ]

        test_course = Course("Test Course", 3)
        run_collection = self.make_run_collection(test_course, obstacle_data)

        test_run = Run(test_course)
        test_run.add_obstacle_time(3)
        test_run.add_obstacle_time(3)

        chance = run_collection.chance_of_personal_best(test_run)

        self.assertTrue(0.48 <= chance <= 0.52)

    def test_chance_of_personal_best_multiple_remaining(self):
        obstacle_data = [
            [3, 3, 2, 3],
            [3, 3, 3, 2],
            [5, 5, 2],
        ]

        test_course = Course("Test Course", 4)
        run_collection = self.make_run_collection(test_course, obstacle_data)

        test_run = Run(test_course)
        test_run.add_obstacle_time(3)
        test_run.add_obstacle_time(3)

        chance = run_collection.chance_of_personal_best(test_run)

        self.assertTrue(0.81333 <= chance <= 0.85333)

    def test_no_complete_run(self):
        obstacle_data = [
            [3, 4],
            [4, 5],
        ]

        test_course = Course("Test Course", 3)
        run_collection = self.make_run_collection(test_course, obstacle_data)

        with self.assertRaises(ValueError):
            run_collection.personal_best()

    def test_best_of_bests_uses_incomplete_runs(self):
        obstacle_data = [
            [5, 5, 5],
            [4, 4, 4],
            [3, 3],
        ]

        test_course = Course("Test Course", 3)
        run_collection = self.make_run_collection(test_course, obstacle_data)

        # O1 min = 3
        # O2 min = 3
        # O3 min = 4
        self.assertEqual(run_collection.best_of_bests(), 10.0)


if __name__ == "__main__":
    unittest.main()
```