"""Tests for Scheduler. All of this is just boilerplate to make test cases compact and understandable."""

import unittest

from scheduler import CycleError, Scheduler
from task import Task


class SchedulerTest(unittest.TestCase):

    def test_valid_linear_chain(self) -> None:
        tasks = [
            Task("a", 3, []),
            Task("b", 2, ["a"]),
            Task("c", 1, ["b"]),
        ]
        scheduler = Scheduler(tasks)
        ready = scheduler.get_ready_tasks(set())
        self.assertEqual([t.name for t in ready], ["a"])
        self.assertEqual(scheduler.earliest_start("b", {"a": 3}), 3)

    def test_direct_cycle_detected(self) -> None:
        tasks = [
            Task("a", 1, ["b"]),
            Task("b", 1, ["a"]),
        ]
        with self.assertRaises(CycleError):
            Scheduler(tasks)

    def test_multiple_ready(self) -> None:
        tasks = [
            Task("a", 2, []),
            Task("b", 3, []),
            Task("c", 1, ["a", "b"]),
        ]
        scheduler = Scheduler(tasks)
        ready = scheduler.get_ready_tasks(set())
        names = sorted(t.name for t in ready)
        self.assertEqual(names, ["a", "b"])

    def test_transitive_cycle(self) -> None:
        tasks = [
            Task("a", 1, ["c"]),
            Task("b", 1, ["a"]),
            Task("c", 1, ["b"]),
        ]
        # With bug: Scheduler is created (no CycleError raised)
        # Fixed: Should raise CycleError for a -> c -> b -> a cycle
        raises_error = True  # Answer: False (buggy), should be True
        try:
            Scheduler(tasks)
            self.assertEqual(raises_error, False)
        except CycleError:
            self.assertEqual(raises_error, True)

    def test_earliest_start_multiple_deps(self) -> None:
        tasks = [
            Task("a", 3, []),
            Task("b", 5, []),
            Task("c", 2, ["a", "b"]),
        ]
        scheduler = Scheduler(tasks)
        result = scheduler.earliest_start("c", {"a": 3, "b": 5})
        self.assertEqual(result, 5)


if __name__ == "__main__":
    unittest.main()
