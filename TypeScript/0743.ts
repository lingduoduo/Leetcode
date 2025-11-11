import { MinPriorityQueue } from "@datastructures-js/priority-queue";

function networkDelayTime(times: number[][], n: number, k: number): number {
  const adj: Map<number, Array<[number, number]>> = new Map();

  // Build adjacency list
  for (const [u, v, w] of times) {
    if (!adj.has(u)) adj.set(u, []);
    adj.get(u)!.push([w, v]); // [weight, target]
  }

  // Min-heap: priority = time
  const heap = new MinPriorityQueue<[number, number]>({
    compare: (a, b) => a[0] - b[0],
  });
  heap.enqueue([0, k]);

  const seen = new Set<number>();
  let time = 0;

  while (!heap.isEmpty()) {
    const [currTime, node] = heap.dequeue();

    if (seen.has(node)) continue;
    seen.add(node);
    time = currTime;

    if (seen.size === n) return time;

    for (const [nextTime, nextNode] of adj.get(node) || []) {
      if (!seen.has(nextNode)) {
        heap.enqueue([currTime + nextTime, nextNode]);
      }
    }
  }

  return -1;
}
