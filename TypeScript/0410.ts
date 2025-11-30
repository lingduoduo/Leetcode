function splitArray(nums: number[], k: number): number {
    let l = Math.max(...nums);
    let r = nums.reduce((a, b) => a + b, 0);

    while (l < r) {
        const mid = l + Math.floor((r - l) / 2); // candidate max subarray sum
        const blocks = split(nums, mid);         // how many blocks needed if max sum <= mid

        if (k < blocks) {
            l = mid + 1;
        } else {
            r = mid;
        }
    }
    return l;
}

function split(nums: number[], bound: number): number {
    let blocks = 1;
    let tot = 0;

    for (const num of nums) {
        if (tot + num > bound) {
            // start a new block with this num
            blocks++;
            tot = num;
        } else {
            tot += num;
        }
    }

    return blocks;
}
