function findDiagonalOrder(mat: number[][]): number[] {
    const d: Map<number, number[]> = new Map();
    for (let i = 0; i < mat.length; i++) {
        for (let j = 0; j < mat[i].length; j++) {
            const key = i + j;
            if (!d.has(key)) {
                d.set(key, []);
            }
            d.get(key)!.push(mat[i][j]);
        }
    }
    const res: number[] = [];
    for (const [key, values] of d.entries()) {
        if (key % 2 === 0) {
            res.push(...values.reverse());
        } else {
            res.push(...values);
        }
    }
    return res;
};