function combine(n: number, k: number): number[][] {
    let res: number[][] = [];

    function dfs(idx: number, path: number[]): void {
        if (path.length === k) {
            res.push([...path]);   // push a copy
            return;                   // <-- keep return inside the if
        }

        for (let i = idx; i <= n; i++) { // iterate 1..n
            path.push(i);                // push element
            dfs(i + 1, path); // next start is i + 1
            path.pop();                  // undo
        }
    }

    dfs(1, []);  // start from 1 with empty path
    return res;
}