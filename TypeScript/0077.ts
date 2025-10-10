function combine(n: number, k: number): number[][] {
    const res: number[][] = [];
    const path: number[] = [];

    function backtrack(start: number): void {
        if (path.length === k) {
            res.push([...path]);     // push a copy
            return;
        }

        // pruning: stop early if not enough numbers left
        for (let i = start; i <= n - (k - path.length) + 1; i++) {
            path.push(i);            // choose
            backtrack(i + 1);        // explore
            path.pop();              // un-choose
        }
    }

    backtrack(1);
    return res;
}
