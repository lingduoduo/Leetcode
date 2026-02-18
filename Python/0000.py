import heapq
from typing import List
import collections
from typing import List, Tuple, Optional

def min_round_trip(depart: List[int], ret: List[int]) -> Tuple[Optional[int], Optional[Tuple[int, int]]]:
    n = min(len(depart), len(ret))
    if n < 2:
        return None, None  # no valid j > i

    best_cost_from = [0] * n
    best_day_from = [0] * n

    best_cost_from[n - 1] = ret[n - 1]
    best_day_from[n - 1] = n - 1

    # build suffix min for return
    for d in range(n - 2, -1, -1):
        if ret[d] <= best_cost_from[d + 1]:
            best_cost_from[d] = ret[d]
            best_day_from[d] = d
        else:
            best_cost_from[d] = best_cost_from[d + 1]
            best_day_from[d] = best_day_from[d + 1]

    ans = float("inf")
    best_pair = None

    for i in range(n - 1):  # i cannot be last day because need j > i
        total = depart[i] + best_cost_from[i + 1]
        j = best_day_from[i + 1]
        if total < ans:
            ans = total
            best_pair = (i, j)

    return ans, best_pair


def run_example(depart: List[int], ret: List[int]) -> None:
    cost, pair = min_round_trip(depart, ret)
    print("depart =", depart)
    print("ret    =", ret)

    if cost is None:
        print("No valid round trip (need return day > depart day).")
        return

    i, j = pair
    print(f"Best cost = {cost}")
    print(f"Best pair = (depart_day={i}, return_day={j})")
    print(f"Check: depart[{i}]={depart[i]} + ret[{j}]={ret[j]} = {depart[i] + ret[j]}")
    print("-" * 50)


if __name__ == "__main__":
    # Example 1
    run_example([5, 3, 4, 8], [6, 10, 2, 7])

    # Example 2 (tie case, return any optimal pair)
    run_example([3, 3, 10, 1], [5, 2, 2, 2])

    # Example 3 (no valid, length < 2)
    run_example([4], [1])



 