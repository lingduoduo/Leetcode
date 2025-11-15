function largestIsland(grid: number[][]): number {
    const n = grid.length;
    if (n === 0) return 0;

    const directions: [number, number][] = [
        [0, 1],
        [0, -1],
        [1, 0],
        [-1, 0],
    ];

    function dfs(x: number, y: number, index: number): number {
        const q: [number, number][] = [[x, y]];
        const visit: Set<string> = new Set();
        visit.add(`${x},${y}`);
        let size = 0;

        while (q.length > 0) {
            const [curx, cury] = q.pop()!;
            grid[curx][cury] = index;
            size++;

            for (const [dx, dy] of directions) {
                const tx = curx + dx;
                const ty = cury + dy;
                if (
                    tx >= 0 && tx < n &&
                    ty >= 0 && ty < n &&
                    grid[tx][ty] === 1
                ) {
                    const key = `${tx},${ty}`;
                    if (!visit.has(key)) {
                        visit.add(key);
                        q.push([tx, ty]);
                    }
                }
            }
        }
        return size;
    }

    const area: Record<number, number> = {};
    let index = 2;

    // Label each island with a unique index and record its area
    for (let i = 0; i < n; i++) {
        for (let j = 0; j < n; j++) {
            if (grid[i][j] === 1) {
                area[index] = dfs(i, j, index);
                index++;
            }
        }
    }

    // In case the grid is all 1s or all 0s
    let res = Math.max(...Object.values(area), 0);

    // Try flipping each 0 to 1 and compute the resulting island size
    for (let i = 0; i < n; i++) {
        for (let j = 0; j < n; j++) {
            if (grid[i][j] === 0) {
                const explore: Set<number> = new Set();
                for (const [dx, dy] of directions) {
                    const tx = i + dx;
                    const ty = j + dy;
                    if (
                        tx >= 0 && tx < n &&
                        ty >= 0 && ty < n &&
                        grid[tx][ty] > 1
                    ) {
                        explore.add(grid[tx][ty]);
                    }
                }

                const newArea =
                    1 + Array.from(explore).reduce((sum, t) => sum + area[t], 0);
                res = Math.max(res, newArea);
            }
        }
    }

    return res;
};
