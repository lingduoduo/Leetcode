"""Runs your Solver. It's useful to see how Solver is called.
You may want to change how Solver is constructed."""

from optimizer import Optimizer
from scheduler import Scheduler
from task import get_test_tasks


def banner(legend: str) -> None:
    border = "#" * (len(legend) + 8)
    print(border)
    print(f"#   {legend}   #")
    print(border)


def main() -> None:
    banner("BEGIN CODE OUTPUT")

    tasks = get_test_tasks()
    scheduler = Scheduler(tasks)
    optimizer = Optimizer(scheduler)

    order = optimizer.topological_sort()
    print("Execution order:")
    for name in order:
        task = scheduler.get_task(name)
        print(f"  {name} (duration={task.duration})")

    total_time, timeline = optimizer.parallel_schedule(num_workers=2)
    print(f"\nParallel schedule (2 workers), total time: {total_time}")
    for name, (start, end) in sorted(timeline.items(), key=lambda x: x[1][0]):
        print(f"  {name}: {start} -> {end}")

    banner("END CODE OUTPUT")


if __name__ == "__main__":
    main()
