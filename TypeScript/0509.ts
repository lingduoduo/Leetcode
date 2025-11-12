function fib(n: number): number {
    if (n <= 1) return n

    let nums = Array(1 + n).fill(0);
    nums[1] = 1;
    for (let i = 2; i < n + 1; i++)
        nums[i] = nums[i - 1] + nums[i - 2];
    return nums[n]
};
