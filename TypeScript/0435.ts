function eraseOverlapIntervals(intervals: number[][]): number {
    intervals.sort((a, b) => (a[0] - b[0]) || (a[1] - b[1]));

    let res = 0;
    for (let i = 1, n = intervals.length, end = intervals[0][1]; i < n; i++) {
        if (end > intervals[i][0]) {
            res++;
            end = Math.min(end, intervals[i][1]);
        } else {
            end = intervals[i][1];
        }
    }
    return res;
};