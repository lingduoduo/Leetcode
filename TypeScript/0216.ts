function combinationSum3(k: number, n: number): number[][] {
    // n = target sum, k = count
    let res: number[][] = [];

    function dfs(target: number, cur: number, idx: number, path: number[]) {
        if (cur > target) return;
        if (path.length === k) {
            if (cur === target) res.push([...path]);
            return;
        }
        for (let i = idx; i <= 9; i++) {
            const next = cur + i;
            if (next > target) break;
            path.push(i);
            dfs(target, next, i + 1, path);
            path.pop();
        }
    }

    dfs(n, 0, 1, []);
    return res;
};