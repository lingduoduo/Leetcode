function pacificAtlantic(heights: number[][]): number[][] {
    const n = heights.length;
    if (n === 0) return [];
    const m = heights[0].length;

    // visited[r][c][sign] where sign: 1 = Pacific (top/left), 0 = Atlantic (bottom/right)
    const visited: [boolean, boolean][][] = Array.from({ length: n }, () =>
        Array.from({ length: m }, () => [false, false])
    );

    const res: number[][] = [];
    const dirs = [[-1, 0], [0, 1], [1, 0], [0, -1]] as const;

    function dfs(x: number, y: number, sign: 0 | 1): void {
        for (const [dx, dy] of dirs) {
            const nx = x + dx;
            const ny = y + dy;
            if (nx < 0 || nx >= n || ny < 0 || ny >= m) continue;
            if (visited[nx][ny][sign]) continue;
            // Reverse flow: can only go to >= height neighbors
            if (heights[nx][ny] < heights[x][y]) continue;

            visited[nx][ny][sign] = true;
            dfs(nx, ny, sign);
        }
    }

    // Seed from left/right borders (Pacific: left -> sign=1, Atlantic: right -> sign=0)
    for (let r = 0; r < n; r++) {
        visited[r][0][1] = true;
        dfs(r, 0, 1);
        visited[r][m - 1][0] = true;
        dfs(r, m - 1, 0);
    }

    // Seed from top/bottom borders (Pacific: top -> sign=1, Atlantic: bottom -> sign=0)
    for (let c = 0; c < m; c++) {
        visited[0][c][1] = true;
        dfs(0, c, 1);
        visited[n - 1][c][0] = true;
        dfs(n - 1, c, 0);
    }

    // Collect cells reachable by both oceans
    for (let r = 0; r < n; r++) {
        for (let c = 0; c < m; c++) {
            if (visited[r][c][0] && visited[r][c][1]) {
                res.push([r, c]);
            }
        }
    }
    return res;
}
