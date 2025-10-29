import { Heap } from "heap-js";

class Solution {
    minMeetingRooms(intervals: number[][]): number {
        if (intervals.length === 0) return 0;
        intervals.sort((a, b) => a[0] - b[0]);

        const heap = new Heap<number>();
        heap.push(intervals[0][1]);
        let res = 1;

        for (let i = 1; i < intervals.length; i++) {
            const [start, end] = intervals[i];
            if (heap.peek() !== undefined && heap.peek()! <= start) {
                heap.pop();
                heap.push(end);
            } else {
                heap.push(end);
                res += 1;
            }
        }
        return res;
    }
}

// Example
const s = new Solution();
console.log(s.minMeetingRooms([[0,30],[5,10],[15,20]])); // 2
