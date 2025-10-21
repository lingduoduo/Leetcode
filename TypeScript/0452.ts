function findMinArrowShots(points: number[][]): number {
    if (points.length === 0) return 0;

    // Sort the points based on the end coordinate
    points.sort((a, b) => a[1] - b[1]);

    let res = 1;
    for (let i = 1, n = points.length, end = points[0][1]; i < n; i++) {
        if (end < points[i][0]) {
            res++;
            end = points[i][1];
        }
        else{
            end = Math.min(end, points[i][1]);
        }
    }
    return res;
};