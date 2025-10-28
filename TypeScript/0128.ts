function longestConsecutive(nums: number[]): number {
    let res = 0;
    const nums_set = new Set<number>();
    for (const num of nums) nums_set.add(num);

    const arr: number[] = [];
    for (const num of nums_set) arr.push(num);

    for (let i = 0; i < arr.length; i++) {
        // start only at the beginning of a streak
        if (nums_set.has(arr[i] - 1)) continue;

        let cnt = 1;
        let cur = arr[i];
        while (nums_set.has(cur + 1)) {
            cur += 1;
            cnt += 1;
        }
        res = Math.max(res, cnt);
    }
    return res;
};
