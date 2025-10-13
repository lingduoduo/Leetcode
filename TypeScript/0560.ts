function subarraySum(nums: number[], k: number): number {
    const freq = new Map<number, number>();
    freq.set(0, 1);              // prefix sum 0 seen once

    let res = 0;
    let cur = 0;

    for (let i = 0; i < nums.length; i++) {
        cur += nums[i];          // prefix sum up to i

        // count subarrays ending at i with sum k
        const need = cur - k;
        res += freq.get(need) ?? 0;

        // record current prefix
        freq.set(cur, (freq.get(cur) ?? 0) + 1);
    }
    return res;
}