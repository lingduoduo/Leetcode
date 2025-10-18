import { PriorityQueue } from '@datastructures-js/priority-queue';

function kSmallestPairs(nums1: number[], nums2: number[], k: number): number[][] {
  const n1 = nums1.length, n2 = nums2.length;
  const res: number[][] = [];
  if (n1 === 0 || n2 === 0 || k <= 0) return res;

  type Node = { i: number; j: number; sum: number };

  // Min-heap by pair sum
  const pq = new PriorityQueue<Node>((a, b) => a.sum - b.sum);

  // Seed: pair each nums1[i] with nums2[0]
  const limit = Math.min(n1, k);
  for (let i = 0; i < limit; i++) {
    pq.enqueue({ i, j: 0, sum: nums1[i] + nums2[0] });
  }

  while (!pq.isEmpty() && res.length < k) {
    const { i, j } = pq.dequeue();
    res.push([nums1[i], nums2[j]]);
    if (j + 1 < n2) {
      pq.enqueue({ i, j: j + 1, sum: nums1[i] + nums2[j + 1] });
    }
  }

  return res;
}