function intervalIntersection(firstList: number[][], secondList: number[][]): number[][] {
    const res: number[][] = [];
    let i = 0, j = 0;

    while (i < firstList.length && j < secondList.length) {
        const [x1, y1] = firstList[i];
        const [x2, y2] = secondList[j]; 
        const left = Math.max(x1, x2);
        const right = Math.min(y1, y2);

        if (left <= right) {
            res.push([left, right]);
        }

        if (y1 < y2) {
            i++;
        } else {
            j++;
        }
    }
    return res;
};
