"""Read this first."""

from functools import lru_cache
from typing import Dict, List, Set, Tuple

from task import Task


class CycleError(Exception):
    pass


class Scheduler:
    def __init__(self, tasks: List[Task]):
        self._tasks: Dict[str, Task] = {t.name: t for t in tasks}
        self._task_names: Tuple[str, ...] = tuple(self._tasks)
        self._dependency_map: Dict[str, Tuple[str, ...]] = {}
        self._task_bits: Dict[str, int] = {}
        self._dependency_masks: Dict[str, int] = {}
        self._zero_dependency_tasks: Tuple[Task, ...] = ()
        self._validate_dependencies()

    def _validate_dependencies(self) -> None:
        dependency_map: Dict[str, Tuple[str, ...]] = {}
        zero_dependency_tasks: List[Task] = []

        for task in self._tasks.values():
            dependencies = tuple(task.depends_on)
            for dep in dependencies:
                if dep not in self._tasks:
                    raise ValueError(f"unknown dependency '{dep}' in task '{task.name}'")

            dependency_map[task.name] = dependencies
            if not dependencies:
                zero_dependency_tasks.append(task)

        self._dependency_map = dependency_map
        self._task_bits = {
            task_name: 1 << index for index, task_name in enumerate(self._task_names)
        }
        self._dependency_masks = {
            task_name: sum(self._task_bits[dep] for dep in dependencies)
            for task_name, dependencies in dependency_map.items()
        }
        self._zero_dependency_tasks = tuple(zero_dependency_tasks)
        self._check_cycles()

    def _check_cycles(self) -> None:
        WHITE, GRAY, BLACK = 0, 1, 2
        colors = {name: WHITE for name in self._task_names}

        for task_name in self._task_names:
            if colors[task_name] != WHITE:
                continue

            stack: List[Tuple[str, bool]] = [(task_name, False)]
            while stack:
                current, exiting = stack.pop()
                color = colors[current]

                if exiting:
                    colors[current] = BLACK
                    continue

                if color == BLACK:
                    continue
                if color == GRAY:
                    raise CycleError(f"cycle detected involving task '{current}'")

                colors[current] = GRAY
                stack.append((current, True))
                for dep_name in reversed(self._dependency_map[current]):
                    dep_color = colors[dep_name]
                    if dep_color == GRAY:
                        raise CycleError(f"cycle detected involving task '{dep_name}'")
                    if dep_color == WHITE:
                        stack.append((dep_name, False))

    def get_task(self, name: str) -> Task:
        return self._tasks[name]

    def get_all_tasks(self) -> List[Task]:
        return list(self._tasks.values())

    @lru_cache(maxsize=None)
    def _ready_task_names(self, completed: frozenset[str]) -> Tuple[str, ...]:
        if not completed:
            return tuple(task.name for task in self._zero_dependency_tasks)

        completed_mask = 0
        for task_name in completed:
            completed_mask |= self._task_bits[task_name]

        ready: List[str] = []
        for task_name in self._task_names:
            task_bit = self._task_bits[task_name]
            if completed_mask & task_bit:
                continue
            if self._dependency_masks[task_name] & completed_mask == self._dependency_masks[task_name]:
                ready.append(task_name)
        return tuple(ready)

    def get_ready_tasks(self, completed: Set[str]) -> List[Task]:
        completed_frozen = frozenset(completed)
        return [self._tasks[name] for name in self._ready_task_names(completed_frozen)]

    def earliest_start(self, name: str, completion_times: Dict[str, int]) -> int:
        dependencies = self._dependency_map[name]
        if not dependencies:
            return 0
        return max(completion_times[dep] for dep in dependencies)
