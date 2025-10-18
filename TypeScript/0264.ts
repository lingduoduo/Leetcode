function nthUglyNumber(n: number): number {
    const ugly: number[] = new Array(n);
    ugly[0] = 1;

    let i2 = 0, i3 = 0, i5 = 0;

    for (let i = 1; i < n; i++) {
        const next2 = ugly[i2] * 2;
        const next3 = ugly[i3] * 3;
        const next5 = ugly[i5] * 5;

        const nextUgly = Math.min(next2, next3, next5);
        ugly[i] = nextUgly;

        if (nextUgly === next2) i2++;
        if (nextUgly === next3) i3++;
        if (nextUgly === next5) i5++;
    }

    return ugly[n - 1];
}
