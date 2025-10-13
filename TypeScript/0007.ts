function reverse(x: number): number {
    const f = x >= 0 ? 1 : -1;
    let num = Math.abs(x);

    // collect digits
    const res: number[] = [];
    while (num > 0) {
        res.push(num % 10);
        num = Math.trunc(num / 10);
    }

    let rev = 0;
    for (let i = 0; i < res.length; i++) {
        rev = rev * 10 + res[i];
    }
    rev *= f;

    if (rev < -(2 ** 31) || rev > 2 ** 31 - 1) return 0;
    return rev;
}