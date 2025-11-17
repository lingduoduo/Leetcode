function findDiagonalOrder(nums: number[][]): number[] {
    const d = new Map<number, number[]>();

    for (let i = 0; i < nums.length; i++) {
        for (let j = 0; j < nums[i].length; j++) {
            const key = i + j;
            if (!d.has(key)) {
                d.set(key, []);
            }
            d.get(key)!.push(nums[i][j]);
        }
    }

    const res: number[] = [];
    const keys = Array.from(d.keys()).sort((a, b) => a - b);
    for (const key of keys) {
        const arr = d.get(key)!;
        for (let i = arr.length - 1; i >= 0; i--) {
            res.push(arr[i]);
        }
    }
    return res;
};
