import { Heap } from 'heap-js';

function kthSmallest(matrix: number[][], k: number): number {
    const m = matrix.length;
    const n = matrix[0].length;

    // min-heap of [value, row, col]
    const heap = new Heap<[number, number, number]>((a, b) => a[0] - b[0]);

    // push first element of each row
    for (let r = 0; r < m; r++) {
        heap.push([matrix[r][0], r, 0]);
    }

    let val = 0;

    // pop k times
    for (let i = 0; i < k; i++) {
        const top = heap.pop();
        if (!top) break; // safety

        const [v, row, col] = top;
        val = v;

        if (col + 1 < n) {
            heap.push([matrix[row][col + 1], row, col + 1]);
        }
    }

    return val;
}
