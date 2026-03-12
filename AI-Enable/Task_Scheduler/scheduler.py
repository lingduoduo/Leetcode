"""Read this first."""

from typing import Dict, List, Set

from task import Task


class CycleError(Exception):
    pass


class Scheduler:
    def __init__(self, tasks: List[Task]):
        self._tasks: Dict[str, Task] = {t.name: t for t in tasks}
        self._validate_dependencies()

    def _validate_dependencies(self) -> None:
        for task in self._tasks.values():
            for dep in task.depends_on:
                if dep not in self._tasks:
                    raise ValueError(f"unknown dependency '{dep}' in task '{task.name}'")
        self._check_cycles()

    def _check_cycles(self) -> None:
        # Use DFS to detect cycles
        WHITE, GRAY, BLACK = 0, 1, 2
        colors = {name: WHITE for name in self._tasks}
        
        def dfs(task_name: str) -> None:
            if colors[task_name] == GRAY:
                raise CycleError(f"cycle detected involving task '{task_name}'")
            if colors[task_name] == BLACK:
                return
                
            colors[task_name] = GRAY
            task = self._tasks[task_name]
            for dep_name in task.depends_on:
                dfs(dep_name)
            colors[task_name] = BLACK
        
        for task_name in self._tasks:
            if colors[task_name] == WHITE:
                dfs(task_name)

    def get_task(self, name: str) -> Task:
        return self._tasks[name]

    def get_all_tasks(self) -> List[Task]:
        return list(self._tasks.values())

    def get_ready_tasks(self, completed: Set[str]) -> List[Task]:
        ready: List[Task] = []
        for task in self._tasks.values():
            if task.name in completed:
                continue
            if all(dep in completed for dep in task.depends_on):
                ready.append(task)
        return ready

    def earliest_start(self, name: str, completion_times: Dict[str, int]) -> int:
        task = self._tasks[name]
        if not task.depends_on:
            return 0
        return max(completion_times[dep] for dep in task.depends_on)
