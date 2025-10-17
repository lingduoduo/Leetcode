function jump(nums: number[]): number {
    const n = nums.length;
    const res = Array(n).fill(Infinity);
    res[0] = 0; // 0 jumps to reach index 0

    for (let i = 0; i < n; i++) {
        if (res[i] === Infinity) continue; // skip unreachable positions
        for (let j = 1; j <= nums[i] && i + j < n; j++) {
            res[i + j] = Math.min(res[i + j], res[i] + 1);
        }
    }
    return res[n - 1];
}