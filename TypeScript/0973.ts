import { Heap } from 'heap-js';

function kClosest(points: number[][], k: number): number[][] {
  // Max-heap (store farthest point on top), that is, [distance, [x, y]]
  const maxHeap = new Heap<[number, number[]]>((a, b) => b[0] - a[0]);

  for (const [x, y] of points) {
    const dist = x * x + y * y;
    maxHeap.push([dist, [x, y]]);
    if (maxHeap.size() > k) maxHeap.pop(); // remove farthest
  }

  return maxHeap.toArray().map(([_, point]) => point);
}