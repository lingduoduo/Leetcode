function merge(intervals: number[][]): number[][] {
    if (intervals.length === 0) return [];
    intervals.sort((a, b) => (a[0] - b[0]));

    let res = [intervals[0]];

    for (let i=1; i<intervals.length; i++){
        const [x1, y1] = res[res.length - 1];
        const [x2, y2] = intervals[i];
        if (y1 < x2) {
            res.push([x2, y2]);
        } else {
            res[res.length - 1][1] = Math.max(y1, y2);
        }
    }

    return res;
};