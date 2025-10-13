function combinationSum2(candidates: number[], target: number): number[][] {
    const res: number[][] = [];
    candidates.sort((a, b) => a - b);

    function dfs(idx: number, remain: number, path: number[]) {
        if (remain === 0) {
            res.push([...path]);            // push a copy
            return;
        }

        if (remain < 0) return;             // overshoot

        for (let i = idx; i < candidates.length; i++) {
            if (i > idx && candidates[i] === candidates[i - 1]) continue;
            path.push(candidates[i]);
            dfs(i + 1, remain - candidates[i], path);
            path.pop();
        }
    }

    dfs(0, target, []);
    return res;
};