"""Tests for Optimizer. Outlines for optional tests, maybe useful after Optimizer is functioning."""

import unittest

from optimizer import Optimizer
from scheduler import Scheduler
from task import get_test_tasks, get_large_tasks


class OptimizerTest(unittest.TestCase):

    def test_topological_sort_basic(self) -> None:
        scheduler = Scheduler(get_test_tasks())
        optimizer = Optimizer(scheduler)
        order = optimizer.topological_sort()
        self.assertEqual(len(order), 5)
        deploy_idx = order.index("deploy")
        test_idx = order.index("test")
        compile_idx = order.index("compile")
        self.assertGreater(deploy_idx, test_idx)
        self.assertGreater(test_idx, compile_idx)

    def test_parallel_schedule_two_workers(self) -> None:
        scheduler = Scheduler(get_test_tasks())
        optimizer = Optimizer(scheduler)
        optimizer.topological_sort()
        total_time, timeline = optimizer.parallel_schedule(num_workers=2)
        self.assertLessEqual(total_time, 10)
        for name, (start, end) in timeline.items():
            task = scheduler.get_task(name)
            self.assertEqual(end - start, task.duration)

    def test_parallel_schedule_large(self) -> None:
        scheduler = Scheduler(get_large_tasks())
        optimizer = Optimizer(scheduler)
        optimizer.topological_sort()
        total_time, timeline = optimizer.parallel_schedule(num_workers=3)
        self.assertLessEqual(total_time, 28)
        for name, (start, end) in timeline.items():
            task = scheduler.get_task(name)
            self.assertEqual(end - start, task.duration)

if __name__ == "__main__":
    unittest.main()
