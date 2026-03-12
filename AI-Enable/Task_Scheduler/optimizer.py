"""You'll implement this."""

from typing import Dict, List, Tuple, Set
from collections import deque
import heapq

from scheduler import Scheduler


class Optimizer:
    def __init__(self, scheduler: Scheduler):
        self.scheduler = scheduler
        self.execution_order: List[str] = []

    def topological_sort(self) -> List[str]:
        """
        Perform topological sort using Kahn's algorithm.
        Returns a valid execution order where dependencies come before dependents.
        """
        # Get all tasks
        all_tasks = self.scheduler.get_all_tasks()
        
        # Build in-degree count for each task
        in_degree = {task.name: len(task.depends_on) for task in all_tasks}
        
        # Initialize queue with tasks that have no dependencies
        queue = deque([task.name for task in all_tasks if len(task.depends_on) == 0])
        
        # Build adjacency list (task -> list of tasks that depend on it)
        dependents = {task.name: [] for task in all_tasks}
        for task in all_tasks:
            for dep in task.depends_on:
                dependents[dep].append(task.name)
        
        self.execution_order = []
        
        while queue:
            current = queue.popleft()
            self.execution_order.append(current)
            
            # Reduce in-degree for all dependents
            for dependent in dependents[current]:
                in_degree[dependent] -= 1
                if in_degree[dependent] == 0:
                    queue.append(dependent)
        
        return self.execution_order

    def parallel_schedule(self, num_workers: int) -> Tuple[int, Dict[str, Tuple[int, int]]]:
        """
        Schedule tasks across multiple workers to minimize total execution time.
        Returns (total_time, timeline) where timeline maps task_name -> (start_time, end_time).
        """
        if not self.execution_order:
            self.topological_sort()
        
        # Track when each worker becomes free
        worker_free_times = [0] * num_workers
        
        # Track completion times for dependency checking
        completion_times = {}
        
        # Timeline to return
        timeline = {}
        
        # Process tasks in topological order
        for task_name in self.execution_order:
            task = self.scheduler.get_task(task_name)
            
            # Find earliest start time based on dependencies
            earliest_start = self.scheduler.earliest_start(task_name, completion_times)
            
            # Find the worker that becomes free earliest
            earliest_worker = 0
            for i in range(1, num_workers):
                if worker_free_times[i] < worker_free_times[earliest_worker]:
                    earliest_worker = i
            
            # Task can start when both dependencies are satisfied AND worker is free
            start_time = max(earliest_start, worker_free_times[earliest_worker])
            end_time = start_time + task.duration
            
            # Update worker availability and completion times
            worker_free_times[earliest_worker] = end_time
            completion_times[task_name] = end_time
            timeline[task_name] = (start_time, end_time)
        
        # Total time is when the last worker finishes
        total_time = max(worker_free_times)
        
        return total_time, timeline

    def get_execution_order(self) -> List[str]:
        return self.execution_order
