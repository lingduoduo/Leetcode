const combinationSum = function (candidates: number[], target: number): number[][] {
    const res: number[][] = [];

    function dfs(idx: number, remain: number, path: number[]) {
        if (remain === 0) {
            res.push([...path]);            // push a copy
            return;
        }
        if (remain < 0) return;             // overshoot

        for (let i = idx; i < candidates.length; i++) {
            path.push(candidates[i]);
            dfs(i, remain - candidates[i], path);
            path.pop();
        }
    }

    dfs(0, target, []);
    return res;
};