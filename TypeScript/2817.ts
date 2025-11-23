import Heap from 'heap-js';

function minAbsoluteDifference(nums: number[], x: number): number {
    const n = nums.length;
    if (x === 0) return 0;

    // Explicitly type the map result as [value, index][]
    const sorted: [number, number][] = nums.map<[number, number]>((val, idx) => [val, idx]);
    sorted.sort((a, b) => a[0] - b[0]); // sort by value

    // leftHeap: min-heap by index j (stores [j, value_j])
    const leftHeap = new Heap<[number, number]>((a, b) => a[0] - b[0]);

    // rightHeap: max-heap by index j via storing -j (stores [-j, value_j])
    const rightHeap = new Heap<[number, number]>((a, b) => a[0] - b[0]);

    // Cast to any so we can call peek(), which exists at runtime
    const leftAny: any = leftHeap;
    const rightAny: any = rightHeap;

    let minDiff = Infinity;

    for (const [val, idx] of sorted) {
        // Push current value+index into both heaps
        leftHeap.push([idx, val]);
        rightHeap.push([-idx, val]);

        // Case 1: indices on the left, j <= idx - x
        while (leftHeap.size() > 0) {
            const top = leftAny.peek() as [number, number]; // [j, v_j]
            if (top[0] + x <= idx) {
                const [, v] = leftHeap.pop()!; // v <= val because we sorted by value
                minDiff = Math.min(minDiff, val - v);
            } else {
                break;
            }
        }

        // Case 2: indices on the right, j >= idx + x
        // condition: (-j) + x <= -idx  ⇔  j >= idx + x
        while (rightHeap.size() > 0) {
            const top = rightAny.peek() as [number, number]; // [-j, v_j]
            if (top[0] + x <= -idx) {
                const [, v] = rightHeap.pop()!;
                minDiff = Math.min(minDiff, val - v);
            } else {
                break;
            }
        }
    }

    return minDiff;
}
